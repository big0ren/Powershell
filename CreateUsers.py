For ($i=0; $i -le 150; $i++) {
    
$temp = @(Get-Content "C:\Users\Administrator\Desktop\users.txt")
$Password = ([char[]]([char]65..[char]95) + ([char[]]([char]97..[char]122)) + 0..9 | sort {Get-Random})[0..8] -join ''
$DepStart = (([char[]]([char]97..[char]100))| sort {Get-Random})[0]

$DepNum = (10..20 | sort {Get-Random})[0]
$indexA = (0..490 | sort {Get-Random})[0]
$indexB = (0..490 | sort {Get-Random})[0]
$fname = $temp[$indexA]
$lname = $temp[$indexB]
$userFname = $fname.ToString().Substring(0,2)
$userLname = $lname.ToString().Substring(0,2)
$username = $DepStart+$DepNum+$userFname+$userLname

Write-Host $username
# Write-Host "For the user: "$username.ToLower()" The first name is: "$fname" and the last name is: " +$lname + " and the password is" + "$Password"


$props=@{
	Name= $fname+" " +$lname
    DisplayName= $fname+" " +$lname
    GivenName= $fname
    Surname = $lname
	AccountPassword=(ConvertTo-SecureString -String $Password -AsPlainText –Force)
	Enabled=$true
	Manager='Administrator'
	title='user'
	POBox='25662'
	ProfilePath="C:\Users\$username"
	SamAccountName=$username
    UserPrincipalName=$username
}
New-ADUser @props
}
