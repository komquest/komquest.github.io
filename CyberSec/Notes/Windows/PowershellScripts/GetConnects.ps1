## Purpose: This will Show you all the "Established" connections on a host while filtering
## out the local connections. Useful for checking to see what proccess are reaching out to
## the webs.
$a = netstat -ano | Select-String 'ESTABLISHED' | ForEach-Object { $_.ToString().Trim() -replace '\s+', ',' } | ConvertFrom-Csv -Header 'Protocol','LocalAddress','ForeignAddress','State','PID'


$e = @()
Foreach ($b in $a) {

	$c = Get-Process -Id $b.PID | Select-Object ProcessName, Id, Path, StartTime
	
	$d = [PSCustomObject]@{

		ProcessName = $c.ProcessName
		Id = $c.Id
		Path = $c.Path
		StartTime = $c.StartTime
		Local = $b.LocalAddress
		Foreign = $b.ForeignAddress
	
	}

	$e += $d


}

$e | Where-Object{$_.Local -notlike "127.0.0.1*" -or $_.Foreign -notlike "127.0.0.1*"} | Format-Table