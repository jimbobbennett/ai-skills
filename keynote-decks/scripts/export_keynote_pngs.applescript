on run argv
	set keyPath to item 1 of argv
	set outDir to item 2 of argv
	set posixFile to POSIX file keyPath

	-- Ensure output folder exists and is empty
	do shell script "rm -rf " & quoted form of outDir & " && mkdir -p " & quoted form of outDir

	tell application "Keynote"
		activate
		set theDoc to open posixFile
		delay 1

		set outFolderFile to POSIX file outDir as alias
		export theDoc to outFolderFile as slide images with properties {image format:PNG, all stages:false, skipped slides:false}

		close theDoc saving no
	end tell

	return "OK: " & outDir
end run
