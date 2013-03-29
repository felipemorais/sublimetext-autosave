# Sublime Text 2 event listeners and commands interface for autosave.

import sublime, sublime_plugin
import os.path
 
settings = sublime.load_settings('AutoSave.sublime-settings')

class AutoSaveEventListener(sublime_plugin.EventListener):

	def on_modified(self, view):
		self.check_save(view)
		print "modified"

	def check_save(self, view):
		listSyntax = settings.get('syntaxAutoSave', False)
		sintax = view.settings().get('syntax').lower()
		exist = False
		for item in enumerate(listSyntax):
			print item[1]
			print sintax;
			print sintax.find(item[1])
			if sintax.find(item[1]) > 0:
				exist = True

		if (exist and view.file_name() and view.is_dirty() and os.path.exists(view.file_name())):
			view.run_command('save');
			print 'save' 