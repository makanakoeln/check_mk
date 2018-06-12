#########################################################
# WSUS sync status script
# 
# used to get the last state of wsus sync on WSUS server
# define port in wsus_sync_status.ini in MK_CONFDIR
# [connection]
# port = 8530
#########################################################

$Computername = 'localhost'
$UseSSL = $False

### get wsus port

if ( Get-ChildItem Env:MK_CONFDIR -ErrorAction SilentlyContinue) 
   {
    $MK_CONFFILE = (Get-ChildItem Env:MK_CONFDIR).Value+"\wsus_sync_status.ini"; 
    if ( Test-Path $MK_CONFFILE) { get-content $MK_CONFFILE | % { if ($_ -match "port = " ) {$port_line = $_ }} }; 
    $port = $port_line.trim("port = ")
   }

### if no mk confdir is found, use wsus standard port

else { $port = "8530" }

Try
{
    [reflection.assembly]::LoadWithPartialName("Microsoft.UpdateServices.Administration") | out-null
    $wsus = [Microsoft.UpdateServices.Administration.AdminProxy]::GetUpdateServer($Computername,$UseSSL,$Port)
}
Catch
{
    $ErrorMessage = $_.Exception.Message
    
}
Finally
{
    "<<<wsus_sync_status>>>"
    if ($wsus) {$wsus.GetSubscription().GetLastSynchronizationInfo() | foreach { 
            $Ende = $_.EndTime
            $Resultat = $_.Result
            }
            $Fin = $Ende.ToString("yyyy-MM-dd HH:mm:ss")
            write-output  Last-Sync" "$env:computername" "$Fin" "$Resultat}
    else { write-output  Last-Sync" "$env:computername" "error:" "$ErrorMessage }
}
