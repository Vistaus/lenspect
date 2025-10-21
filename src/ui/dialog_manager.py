# dialog_manager.py
#
# Copyright 2025 Vladimir Kosolapov
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gtk

class DialogManager:
    def __init__(self, parent):
        self.parent = parent

    def show_error(self, title: str, message: str):
        dialog = Adw.AlertDialog.new(title, message)
        dialog.add_response("ok", _('OK'))
        dialog.present(self.parent)

    def show_api_help(self):
        message = _('To use Lenspect, you need a public VirusTotal API key:\n\n'
            '1. Go to {link}\n'
            '2. Create a free account\n'
            '3. Open your profile settings\n'
            '4. Copy personal API key\n'
            '5. Paste it in the Lenspect').format(
            link = '<a href="https://www.virustotal.com">virustotal.com</a>')

        dialog = Adw.AlertDialog.new(_('Get VirusTotal API Key'), message)
        dialog.set_body_use_markup(True)
        dialog.add_response("cancel", _('Close'))
        dialog.add_response("open", _('Documentation'))
        dialog.set_response_appearance("open", Adw.ResponseAppearance.SUGGESTED)
        dialog.connect("response", self.on_api_help_response)
        dialog.present(self.parent)

    def on_api_help_response(self, dialog, response):
        if response == "open":
            Gtk.UriLauncher.new(
                "https://docs.virustotal.com/docs/please-give-me-an-api-key"
            ).launch(self.parent, None, None, None)
