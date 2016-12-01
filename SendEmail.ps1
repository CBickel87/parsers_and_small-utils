$To = "First Last <first.last@email.com>"
$From = "FromAddress <from.address@email.com>"
$Cc = "First Last <first.last@email.com>"
$Subject = "Outdated Reports on Server"
$body = @"
Detected outdated reports:
\\Server\Folder\ "outdated_reports.txt"

This script originates from \\Server\ScriptsFolder
"@

Send-MailMessage -To $To  -From $From -Cc $Cc -Subject $Subject -body $body -SmtpServer "emailserver.domain.com"