from devassistant.assistant_base import AssistantBase

class PythonAssistant(object):
    name = 'base'
    verbose_name = 'Base'
    needs_sudo = False

    args = []
    usage_string_fmt = 'Usage of {verbose_name}:'