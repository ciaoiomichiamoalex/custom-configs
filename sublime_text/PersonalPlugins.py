import sublime
import sublime_plugin


class TrimCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel() if not all(r.empty() for r in self.view.sel()) else [sublime.Region(0, self.view.size())]
        for region in regions:
            text = '\n'.join(row.strip() for row in self.view.substr(region).splitlines() if row.strip())
            self.view.replace(edit, region, text)

class OnRowStringCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel() if not all(r.empty() for r in self.view.sel()) else [sublime.Region(0, self.view.size())]
        for region in regions:
            text = "'" + "', '".join(row.strip() for row in self.view.substr(region).splitlines() if row.strip()) + "'"
            self.view.replace(edit, region, text)

class OnRowNumberCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.sel() if not all(r.empty() for r in self.view.sel()) else [sublime.Region(0, self.view.size())]
        for region in regions:
            text = ', '.join(row.strip() for row in self.view.substr(region).splitlines() if row.strip())
            self.view.replace(edit, region, text)
