on run argv
	set keyPath to item 1 of argv
	set posixFile to POSIX file keyPath

	tell application "Keynote"
		activate
		set theDoc to open posixFile
		delay 1

		set themeName to name of document theme of theDoc
		set slideWidth to width of theDoc
		set slideHeight to height of theDoc

		-- Master slide names
		set masterNames to {}
		repeat with m in slide layouts of theDoc
			set end of masterNames to name of m
		end repeat

		-- Slide 1 details (title slide of reference)
		set firstMaster to ""
		try
			set firstMaster to name of base slide of slide 1 of theDoc
		end try

		close theDoc saving no
	end tell

	set AppleScript's text item delimiters to ", "
	set masterList to masterNames as string
	set AppleScript's text item delimiters to ""

	return "Theme: " & themeName & linefeed & ¬
		"Size: " & slideWidth & " x " & slideHeight & linefeed & ¬
		"Slide 1 master: " & firstMaster & linefeed & ¬
		"All masters: " & masterList
end run
