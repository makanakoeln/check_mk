Function regValueExists (key)
      'This function checks if a registry value exists and returns True of False
      On Error Resume Next
      Dim oShell
      Set oShell = CreateObject ("WScript.Shell")
      regValueExists = True
      Err.Clear
      oShell.RegRead(key)
      If Err <> 0 Then regValueExists = False
      Err.Clear
      Set oShell = Nothing
End Function

If regValueExists("HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\Results\Install\LastSuccessTime") Then
      Dim ObjShell
      Dim ShellObject 
      Set ShellObject = CreateObject("WScript.Shell")
      Set ObjShell = CreateObject("WScript.Shell")
      ObjShell = ShellObject.RegRead("HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\Results\Install\LastSuccessTime")

      output = ""
      Sub addOutput(text)
          output = output & text & vbLf
      End Sub

      addOutput( "<<<last_windows_updates>>>" )
      addOutput(ObjShell)

      WScript.echo output
Else
      output = ""
      addOutput( "<<<last_windows_updates>>>" )
      addOutput( "Registry Key nicht gefunden" )
      WScript.echo output
End If

