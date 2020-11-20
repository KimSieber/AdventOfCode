Option Explicit
'#####################################
'##### Advent of Code
'#####
'##### Day 5: Sunny with a Chance of Asteroids
'##### Intcode Computer - 2.
'#####################################
'##### Erklärung Bedeutung Command
'##### ABCDE
'#####  1002
'#####
'##### DE - two-digit opcode,      02 == opcode 2
'##### C - mode of 1st parameter,  0 == position mode
'##### B - mode of 2nd parameter,  1 == immediate mode
'##### A - mode of 3rd parameter,  0 == position mode,
'#####                                   omitted due to being a leading zero
'##### Eingabewerte
Const INPUTFILENAME = "C:\test\input.txt"
'Const INPUTLINE = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,6,23,2,23,6,27,2,6,27,31,2,13,31,35,1,9,35,39,2,10,39,43,1,6,43,47,1,13,47,51,2,6,51,55,2,55,6,59,1,59,5,63,2,9,63,67,1,5,67,71,2,10,71,75,1,6,75,79,1,79,5,83,2,83,10,87,1,9,87,91,1,5,91,95,1,95,6,99,2,10,99,103,1,5,103,107,1,107,6,111,1,5,111,115,2,115,6,119,1,119,6,123,1,123,10,127,1,127,13,131,1,131,2,135,1,135,5,0,99,2,14,0,0"
'Const INPUTLINE = "3,0,4,0,99"
'Const INPUTLINE = "1002,4,3,4,33"
'Const INPUTLINE = "1101,100,-1,4,0"
'Const INPUTLINE = "3,9,8,9,10,9,4,9,99,-1,8"
'                  0 1 2 3  4 5 6 7  8  9 10
'                  3,9,8,9,10,9,4,9,99,-1, 8    -> Start
'                  3,9,8,9,10,9,4,9,99, 8, 8    -> Eingabe: 8 -> Speicher auf Pos9
'                  3,9,8,9,10,9,4,9,99, 1, 8    -> Pos9=Pos10, dann Pos9=1
'                  3,9,8,9,10,9,4,9,99, 1, 8    -> Ausgabe Pos9 = 1
'Const INPUTLINE = "3,9,7,9,10,9,4,9,99,-1,8"
'Const INPUTLINE = "3,3,1108,-1,8,3,4,3,99"
'Const INPUTLINE = "3,3,1107,-1,8,3,4,3,99"
'Const INPUTLINE = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
'################################################################################################################
'                   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99,-1, 0, 1, 9   -> Start
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99, 0, 0, 1, 9   -> Input=0 -> speichern auf Pos12=0
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99, 0, 0, 1, 9   -> Pos12=0 -> Springe auf Pos9 (Wert von Pos15)
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99,-1, 0, 1, 9   -> Output Pos13 = 0
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99,-1, 0, 1, 9   -> ENDE
'################################################################################################################
'                   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99,-1, 0, 1, 9   -> Start
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99, 1, 0, 1, 9   -> Input=1 -> speichern auf Pos12=1
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99, 0, 0, 1, 9   -> Pos12=1 -> keine Aktion
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99, 0, 1, 1, 9   -> Addiere Pos13=0 + Pos14=1 = Pos13=1
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99,-1, 0, 1, 9   -> Ausgabe Pos13=1
'                   3,12, 6,12,15, 1,13,14,13, 4,13,99,-1, 0, 1, 9   -> ENDE
'Const INPUTLINE = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
Const INPUTLINE = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"

Sub workingComputer()
    '##### Werte in Array laden
    Dim vValues As Variant
    vValues = Split(loadInput(), ",")
    'vValues = Split(INPUTLINE, ",")
    '##### Manipulation zweier Werte (Vorgabe aus Aufgabe Day 2)
    'vValues(1) = 12
    'vValues(2) = 2
    Dim vTargetPos As Long
    Dim vFirstValue As Long
    Dim vSecondValue As Long
    Dim i, y As Integer
    Dim vInstruction As String * 5
    For i = 0 To UBound(vValues)
        vInstruction = Right("0000" & vValues(i), 5)
        y = 0
        If Int(Right(vInstruction, 2)) = 99 Then Exit For
        Select Case (Int(Right(vInstruction, 2)))
            Case 1, 2, 3, 4, 5, 6, 7, 8
                If Mid(vInstruction, 3, 1) = 0 Then vFirstValue = Int(vValues(vValues(i + 1))) Else vFirstValue = Int(vValues(i + 1))
                y = y + 1
        End Select
        Select Case (Int(Right(vInstruction, 2)))
            Case 1, 2, 5, 6, 7, 8
                If Mid(vInstruction, 2, 1) = 0 Then vSecondValue = Int(vValues(vValues(i + 2))) Else vSecondValue = Int(vValues(i + 2))
                y = y + 1
        End Select
        Select Case (Int(Right(vInstruction, 2)))
            Case 1, 2, 7, 8
                If Left(vInstruction, 1) = 0 Then vTargetPos = vValues(i + 3) Else MsgBox "ERROR"
                y = y + 1
        End Select
        Select Case (Int(Right(vInstruction, 2)))
            Case 1
                vValues(vTargetPos) = vFirstValue + vSecondValue
            Case 2
                vValues(vTargetPos) = vFirstValue * vSecondValue
            Case 3
                vValues(vValues(i + 1)) = Int(InputBox("Bitte Zahl eingeben:"))
            Case 4
                MsgBox "Zahl ausgeben: " & vFirstValue
            Case 5
                If vFirstValue <> 0 Then i = vSecondValue - 1 - y
            Case 6
                If vFirstValue = 0 Then i = vSecondValue - 1 - y
            Case 7
                If vFirstValue < vSecondValue Then vValues(vTargetPos) = 1 Else vValues(vTargetPos) = 0
            Case 8
                If vFirstValue = vSecondValue Then vValues(vTargetPos) = 1 Else vValues(vTargetPos) = 0
            Case Else
                MsgBox "ERROR" & Chr(10) & _
                       "Unknown Instruction" & Chr(10) & _
                       "vValues(" & i & ") = " & vValues(i)
                Exit For
        End Select
        'Stop
        i = i + y
    Next i
    '##### Testweise Ausgabe des Arrays (nur bei kleinen Arrays zum Test möglich)
    'MsgBoxValues (vValues)
    MsgBox "ENDE" ' & Chr(10) & _
           '"vValues(0) = " & vValues(0)
End Sub

Function loadInput() As String
    Open INPUTFILENAME For Input As #1
    Line Input #1, loadInput
    Close #1
End Function

Sub MsgBoxValues(pValues As Variant)
    Dim vText As String
    Dim i As Integer
    For i = 0 To UBound(pValues)
        vText = vText & Chr(10) & "Values(" & i & ") = " & pValues(i)
    Next
    MsgBox vText
End Sub
