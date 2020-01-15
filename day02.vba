'#####################################
'##### Advent of Code
'#####
'##### Day 2: 1202 Program Alarm
'##### Working Computer - Gravity
'#####################################
'##### Eingabewerte
Const INPUTLINE = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,6,23,2,23,6,27,2,6,27,31,2,13,31,35,1,9,35,39,2,10,39,43,1,6,43,47,1,13,47,51,2,6,51,55,2,55,6,59,1,59,5,63,2,9,63,67,1,5,67,71,2,10,71,75,1,6,75,79,1,79,5,83,2,83,10,87,1,9,87,91,1,5,91,95,1,95,6,99,2,10,99,103,1,5,103,107,1,107,6,111,1,5,111,115,2,115,6,119,1,119,6,123,1,123,10,127,1,127,13,131,1,131,2,135,1,135,5,0,99,2,14,0,0"

Sub workingComputer()
    '##### Werte in Array laden
    Dim vValues As Variant
    vValues = Split(INPUTLINE, ",")
    '##### Manipulation zweier Werte
    vValues(1) = 12
    vValues(2) = 2
    Dim i As Integer
    For i = 0 To UBound(vValues)
        Select Case (vValues(i))
        Case 1
            vValues(vValues(i + 3)) = Int(vValues(vValues(i + 1))) + Int(vValues(vValues(i + 2)))
            i = i + 3
        Case 2
            vValues(vValues(i + 3)) = Int(vValues(vValues(i + 1))) * Int(vValues(vValues(i + 2)))
            i = i + 3
        Case 99
            Exit For
        Case Else
            MsgBox "ERROR" & Chr(10) & _
                   "Unknown Instruction" & Chr(10) & _
                   "vValues(" & i & ") = " & vValues(i)
        End Select
    Next i
    MsgBox "ENDE" & Chr(10) & _
           "vValues(0) = " & vValues(0)
End Sub
