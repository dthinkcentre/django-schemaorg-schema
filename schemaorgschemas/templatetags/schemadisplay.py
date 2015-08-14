from django.conf import settings
from django import template
from django.template import Library, NodeList
from django.template.base import TemplateSyntaxError, TextNode, Node
from formatters import SchemaPropFormatter, EnumPropFormatter
from django.db.models.loading import get_model
import sys
from fileinput import lineno

SCHEME = getattr(settings, "SCHEME", "http://")

register = Library()

VOID_ELEMENTS = ["<area ", "<base ", "<br>", "<col ", "<command ", "<embed ", "<hr>", "<img ", "<input ", "<keygen ", "<link ", "<meta ", "<param ", "<source ", "<track ", "<wbr"]
FILE_FIELD_SPECIALS = ['.url', '.path']


class ReturnedRender(object):

    def __init__(self, rendered):
        self._rendered = rendered
        self._normal = True

    def __str__(self):
        return self._rendered

    def __unicode__(self):
        return str(self._rendered)

    @property
    def normal(self):
        return self._normal

    @normal.setter
    def noraml(self, value):
        self._normal = value
    
    
    


@register.simple_tag(takes_context=False)
def schemaprop(item, field_name=None):
    """takes an instance of an model object and field name
    and returns the schema.org property and value formatted
    version where appropriate.
    """
    magix = None
    if not field_name:
        raise TemplateSyntaxError('need to specify field name')
    if field_name[-8:] == '_display' and field_name[:4] == 'get_':
        cut_name = field_name[4:-8]
        try:
            store_value = getattr(item, cut_name)
            field_name = cut_name
        except:
            raise TemplateSyntaxError("SchemaError, " + field_name + "not in SchemaFields")
    if "." in field_name:
        find_point = field_name.find(".")
        try:
            new_item = getattr(item, field_name[:find_point])
            new_field_name = field_name[find_point + 1:]
            return schemaprop(new_item, new_field_name)
        except:
            for last_check in FILE_FIELD_SPECIALS:
                if field_name[-len(last_check):] == last_check:
                    new_field_name = field_name[:-len(last_check)]
                    return schemaprop(item, new_field_name)
    try:
        store_value = getattr(item, field_name)
    except:
        raise TemplateSyntaxError("SchemaError, " + field_name + " not in SchemaFields")
    if callable(store_value):
        ret = ReturnedRender(store_value())
        ret.noraml = False
        return ret
    schema = getattr(item.SchemaFields, field_name)
    format_as = schema._format_as
    if (schema._format_as == 'ForeignKey'):
        if (schema.traceback is True):
            f_obj = getattr(item, field_name)
            item_scope = schemascope(f_obj)
            if item_scope:
                store_value = item_scope
            else:
                format_as = 'default'
        else:
            format_as = 'default'
    if schema._format_as == 'enum':
        magix = EnumPropFormatter(schema=schema)
    if not magix:
        magix = SchemaPropFormatter(schema=schema)
    magix.format_as = format_as
    magix.value = store_value
    ret = ReturnedRender(magix.render())
    return ret


@register.simple_tag(takes_context=False)
def schemascope(item):
    """
    Takes instance of model object and includes the schema.org url
    If there's an internal url that is also included.
    """
    ret = ''
    url = ''
    try:
        ret = '"' + item.schema_url + '"'
    except:
        # not a schemascope item
        return ''
    try:
        url = item.get_absolute_url()
    except:
        return ret
    if url:
        ret = ret + ' link="' + SCHEME + item.site.domain + url + '"'
    return ret


@register.tag(name="schemaobject")
def do_schema_render(parser, token):
    """
    The schemaobject and endschemaobject tag replace the html element that contains the object.
    This is then provided as the second argument should the default 'section' not be desired.
    The third optional parameter is contained inside quotes is the html class details.
    The forth option allows the use of ids for the section,  appending the object.pk to the id text
    {% schemaobject object section "class='otherstuff'" 'obj' %}
    The all fields that have relevant schema.org information associated through their SchemaFields will have the schema.org information inserted into the HTML.
    """
    token = token.split_contents()
    nodelist = parser.parse(('endschemaobject',))
    parser.delete_first_token()
    # defaults the HTML class to section unless over-ride specified
    section = 'section'
    htmlattr = None
    id_attr = None
    c = token.__len__()
    if c > 2:
        section = token[2]
    if c > 3:
        htmlattr = token[3]
        # remove quotes
        htmlattr = htmlattr[1:-1]
    if c > 4:
        id_attr = token[4]
        id_attr = id_attr[1:-1]
    rets = SchemaNode(nodelist, token[1], section, htmlattr, id_attr)
    return rets


class SchemaNode(template.Node):

    def __init__(self, nodelist, object_name, html_class=None,
                 html_attribute=None, id_attr=None):
        self.nodelist = nodelist
        self.object_name = object_name
        self.html_class = html_class
        self.html_attribute = html_attribute
        self.id_attr = id_attr

    @staticmethod
    def split_text_node(text_node_string):
        f = text_node_string.find('>')
        o_f = 0
        item = text_node_string[0:f + 1]
        output = [TextNode(item)]
        while True:
            o_f = f
            f = text_node_string.find('>', o_f + 1)
            if f == -1:
                item = TextNode(text_node_string[o_f + 1:])
            else:
                item = TextNode(text_node_string[o_f + 1: f + 1])
            if item.s:
                output.append(item)
            if f == -1:
                return output

    def get_context_object(self, context):
        i = context.dicts.__len__() - 1
        # going backwards as it seems the information is stored in the last
        while i >= 0:
            dic = context.dicts[i]
            obj = dic.get(self.object_name, None)
            if obj:
                return obj
            i = i - 1
        if not obj:
            raise TemplateSyntaxError(
                self.object_name +
                ' not found in template context')

    @staticmethod
    def strip_annoying_text(text_to_strip, text_replace=''):
        text_to_strip = text_to_strip.replace("<", "")
        text_to_strip = text_to_strip.replace(">", "")
        text_to_strip = text_to_strip.replace(text_replace, "")
        text_to_strip = text_to_strip.strip("\r\n")
        return text_to_strip

    def assemble_for_node(self, node, context):
        if self.object_name not in str(node.sequence):
            return node
        sub_obj = str(node.sequence).replace(self.object_name + '.', '')
        sfind = sub_obj.find("_")
        if sfind != -1:
            sub_obj = sub_obj[:sfind]
        my_model = get_model(self.obj._meta.app_label, sub_obj)
        if not my_model:
            sfind = sub_obj.find(".")
            if sfind != -1:
                sub_obj = sub_obj[:sfind]
            my_model = get_model(self.obj._meta.app_label, sub_obj)
        if not my_model:
            obj_manager = getattr(self.obj, sub_obj)
            my_model = obj_manager.model
        # see if the object is actually a manager rather than a field
        schema_model = my_model.objects.all()[0]
        if not hasattr(my_model, 'SchemaFields'):
            return node
        new_nodes = self.process_node_list(node.nodelist_loop, context)
        section_text = ""
        while "/" not in section_text:
            end = new_nodes.pop()
            section_text = end.s
        section_text = self.strip_annoying_text(section_text, "/")
        top = new_nodes.pop(0)
        top_text = top.s
        top_text = self.strip_annoying_text(top_text, section_text)
        schema_prop = getattr(self.obj.SchemaFields, sub_obj, "")
        if schema_prop:
            top_text = top_text + ' itemprop="' + schema_prop.schema_prop + '"'
        outlist = []
        filter_dict = {}
        if hasattr(self.obj, sub_obj + '_set'):
            attrholder = getattr(self.obj, sub_obj + '_set')
            filter_dict = attrholder.core_filters
        if not filter_dict.__len__():
            if hasattr(self.obj, sub_obj):
                # manager
                filter_dict = getattr(self.obj, sub_obj).core_filters
        if filter_dict:
            schema_models = my_model.objects.filter(**filter_dict)
            for schema_model in schema_models:
                context.update({node.loopvars[0]: schema_model})
                output = SchemaNode(new_nodes, node.loopvars[0], section_text, top_text)
                outlist.append(output)
        node.nodelist = outlist
        return node

    def assemble_if_node(self, node, context):
        new_conditions = []
        # iterate through list
        for condition in node.conditions_nodelists:
            # condition is tuple index 0 points to a template literal object
            # index 1 points to a NodeList
            t_lit = condition[0]
            new_nodes = self.process_node_list(condition[1], context)
            new_conditions.append((t_lit, new_nodes))
        node.conditions = new_conditions
        return node

    def process_node_list(self, nodelist, context):
        new_nodes = NodeList()
        variable_nodes = []
        i = nodelist.__len__() - 1
        l = 0
        while l <= i:
            while l <= i:
                this_node = nodelist[l]
                node_class = this_node.__class__.__name__
                if node_class == "ForNode":
                    this_node = self.assemble_for_node(this_node, context)
                if node_class == "IfNode":
                    this_node = self.assemble_if_node(this_node, context)
                if node_class == 'TextNode':
                    splitted = self.split_text_node(this_node.s)
                    for item in splitted:
                        new_nodes.append(item)
                else:
                    new_nodes.append(this_node)
                if "VariableNode" in node_class:
                    variable_nodes.append(new_nodes.__len__() - 1)
                l = l + 1
            for item in variable_nodes:
                node_in_question = new_nodes[item]
                schema_prop = ''
                if hasattr(node_in_question, 'filter_expression'):
                    filter_exp = str(node_in_question.filter_expression)
                    filter_exp = filter_exp.replace(self.object_name + '.', '')
                    # ensure ones with added template tags work properly
                    if '|' in filter_exp:
                        filter_exp = filter_exp[:filter_exp.find('|')]
                    try:
                        schema_prop = schemaprop(self.obj, filter_exp)
                    except:
                        e = sys.exc_info()[0]
                        raise TemplateSyntaxError(e)
                if schema_prop.normal:
                    prior_node_counter = 1
                    prior_node = new_nodes[item - prior_node_counter]
                    prior_node_text = prior_node.s
                    # this could do with a rewrite to better deal with <a href="{{object.get_absolute_url">{{object.text}}</a> which currently requires <span>{{object.text}}</span>
                    while "<" not in prior_node_text:
                        prior_node_counter = prior_node_counter + 1
                        prior_node = new_nodes[item - prior_node_counter]
                        if hasattr(prior_node, "s"):
                            prior_node_text = prior_node.s
                    if any(void in prior_node_text for void in VOID_ELEMENTS):
                        cutter = prior_node_text.find(" ")
                    else:
                        cutter = prior_node_text.find(">")
                    prior_node.s = prior_node_text[:cutter] + ' ' + str(schema_prop) + prior_node_text[cutter:]
                else:
                    pass
            scope = schemascope(self.obj)
            top_text = "<" + self.html_class + ' '
            if self.html_attribute:
                top_text = top_text + self.html_attribute
            if self.id_attr:
                top_text = top_text + ' id="#' + self.id_attr + str(self.obj.pk) + '"'
            top_text = top_text + ' itemscope itemtype=' + scope + '>'
            bottom_text = "</" + self.html_class + ">"
            topnode = TextNode(top_text)
            bottomnode = TextNode(bottom_text)
            new_nodes.insert(0, topnode)
            new_nodes.append(bottomnode)
        return new_nodes

    def render(self, context):
        self.obj = self.get_context_object(context)
        new_nodes = self.process_node_list(self.nodelist, context)
        output = new_nodes.render(context)
        return output
