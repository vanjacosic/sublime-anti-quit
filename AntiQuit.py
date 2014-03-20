import sublime, sublime_plugin

class AntiQuit(sublime_plugin.TextCommand):
    def run(self, edit):
        confirmation = sublime.ok_cancel_dialog("Are you sure you want to quit?")

        if confirmation is True:
            sublime.run_command('exit')
