'#####################################
'##### Advent of Code
'#####
'##### Day 4: Secure Container
'#####################################
Const STARTDIGIT = 387638
Const ENDDIGIT = 919123
Const OUTPUTFILE = "C:\test\digitlist.txt"

Sub starten()
    Dim i As Long
    Dim n As Long
    n = 0
    Open OUTPUTFILE For Output As #1
    For i = STARTDIGIT To ENDDIGIT
        If checkAscendingDigits(i) = True Then
            If checkDigitsDouble(i) = True Then
                n = n + 1
                Print #1, "#" & Right("000000" & n, 4) & "    "; i
            End If
        End If
    Next
    Close #1
    MsgBox "END" & Chr(10) & "n=" & n
End Sub

Function checkAscendingDigits(i As Long) As Boolean
    If Mid(i, 1, 1) <= Mid(i, 2, 1) And _
       Mid(i, 2, 1) <= Mid(i, 3, 1) And _
       Mid(i, 3, 1) <= Mid(i, 4, 1) And _
       Mid(i, 4, 1) <= Mid(i, 5, 1) And _
       Mid(i, 5, 1) <= Mid(i, 6, 1) Then
         checkAscendingDigits = True
    Else
        checkAscendingDigits = False
    End If
End Function

Function checkDigitsDouble(vDigits As Long)
    checkDigitsDouble = False
    '###### Zähler für Zahlen
    '###### vDigitCounter(0...9) = value
    '###### value = Zähler, Anzahl Ziffer in Digits (0....6)
    Dim vDigitCounter(10) As Integer
    Dim i As Integer
    '###### Ziffern durchgehen und zählen
    For i = 1 To 6
        vDigitCounter(Mid(vDigits, i, 1)) = vDigitCounter(Mid(vDigits, i, 1)) + 1
    Next
    '##### Prüfen, ob (mindestens) zwei doppelte vorhanden
    For i = 0 To 9
        '################################################
        '##### PART ONE: mindestens zwei gleiche Ziffern
        'If vDigitCounter(i) >= 2 Then
        '################################################
        '##### PART TWO: genau zwei gleiche Ziffern
        If vDigitCounter(i) = 2 Then
            checkDigitsDouble = True
            Exit For
        End If
    Next
    'MsgBox "checkDigitsDouble=" & checkDigitsDouble & Chr(10) & _
           "0 = " & vDigitCounter(0) & Chr(10) & _
           "1 = " & vDigitCounter(1) & Chr(10) & _
           "2 = " & vDigitCounter(2) & Chr(10) & _
           "3 = " & vDigitCounter(3) & Chr(10) & _
           "4 = " & vDigitCounter(4) & Chr(10) & _
           "5 = " & vDigitCounter(5) & Chr(10) & _
           "6 = " & vDigitCounter(6) & Chr(10) & _
           "7 = " & vDigitCounter(7) & Chr(10) & _
           "8 = " & vDigitCounter(8) & Chr(10) & _
           "9 = " & vDigitCounter(9)
End Function
