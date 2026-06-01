on run argv
	set keyPath to item 1 of argv
	set outPath to item 2 of argv
	set posixFile to POSIX file keyPath

	tell application "Keynote"
		activate
		set theDoc to open posixFile
		delay 1

		set outLines to {}
		set slideCount to count of slides of theDoc
		set end of outLines to "# Slide count: " & slideCount
		set end of outLines to ""

		repeat with i from 1 to slideCount
			set s to slide i of theDoc
			set slideTitle to ""
			set slideBody to ""
			set slideNotes to ""

			try
				set slideTitle to object text of default title item of s as string
			end try
			try
				set slideBody to object text of default body item of s as string
			end try
			try
				set slideNotes to presenter notes of s as string
			end try

			set end of outLines to "## Slide " & i
			set end of outLines to "### Title"
			set end of outLines to slideTitle
			set end of outLines to "### Body"
			set end of outLines to slideBody
			set end of outLines to "### Notes"
			set end of outLines to slideNotes
			set end of outLines to ""
		end repeat

		close theDoc saving no
	end tell

	set AppleScript's text item delimiters to (ASCII character 10)
	set outText to outLines as string
	set AppleScript's text item delimiters to ""

	set fh to open for access (POSIX file outPath) with write permission
	set eof fh to 0
	write outText to fh as «class utf8»
	close access fh

	return "OK: " & outPath
end run
