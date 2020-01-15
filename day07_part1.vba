Option Explicit
'#####################################
'##### Advent of Code
'#####
'##### Day 7: Amplification Circuit
'##### Intcode Computer - 3.
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
Const INPUTFILENAME = "C:\test\inputtest5.txt"
Const SEQUENCEBEGIN = 5
Const SEQUENCEEND = 9

Sub start()
    '##### Lade Programm
    Dim vProgramm As Variant
    vProgramm = Split(loadInput(), ",")
    '##### Phase-Sequence definieren
    '##### Alle mögichen Sequences ermitteln
    Dim vSequences As Variant
    vSequences = getCombinations(SEQUENCEBEGIN, SEQUENCEEND)
    '##### Intcode-Computer mit allen möglichen Sequences durchlaufen
    Dim i As Integer
    Dim vPhaseSequence As Variant
    Dim vReturnValue As Long
    Dim vHighestReturnValue As Long
    vHighestReturnValue = 0
    Dim vStartValue As Long
    vStartValue = 0
    For i = 0 To UBound(vSequences, 1)
        vPhaseSequence = Array(vSequences(i, 0), vSequences(i, 1), vSequences(i, 2), vSequences(i, 3), vSequences(i, 4))
        vReturnValue = runIncodeComputerWithParameters(vProgramm, vPhaseSequence, vStartValue)
        If vReturnValue > vHighestReturnValue Then vHighestReturnValue = vReturnValue
    Next i
    MsgBox "Höchter Wert:           " & vHighestReturnValue
End Sub

'#####################################################################################################
'###### LOAD INPUT
'######
'###### Lädt in Konstante definierte Datei
'###### und gibt erste Zeile dieser Datei zurück
'#####################################################################################################
Function loadInput() As String
    Open INPUTFILENAME For Input As #1
    Line Input #1, loadInput
    Close #1
End Function

'#####################################################################################################
'###### ALLE KOMBINATIONEN VON 0..4 ZURÜCKGEBEN
'######
'###### Gibt ein 2-dimensionales Array zurück mit allen Kombinationen aus den 5 Ziffern n..m
'######
'###### Parameter #1: pStartValue     Integer, welches den Start-Wert angibt, e.g. 0
'###### Parameter #2: pInputs         Integer, welches den End-Wert angibt, e.g. 4
'###### -> ACHTUNG: Nur Ziffern mit Differenz 4, also 5 Ziffern angeben
'######
'###### ReturnValue(0..n, 0..4) = Wert von 0..4
'###### -> 0..n = Anzahl an eindeutigen Kombinationen
'###### -> 0..4 = Alle Werte 0..4 in einer Reihe sind nur einmalig vorhanden (keine doppelte 1, 2, usw.
'#####################################################################################################
Function getCombinations(pStartValue As Integer, pEndValue As Integer) As Variant
    Dim i, j, k, l, m, a, b, c As Integer
    Dim vReturnStrings As Variant
    ReDim vReturnStrings(0)
    a = -1
    '##### Bildung aller Kombinationen aus 0..4 in String setzen und in Liste (Array speichern)
    For i = pStartValue To pEndValue
        For j = pStartValue To pEndValue
            For k = pStartValue To pEndValue
                For l = pStartValue To pEndValue
                    For m = pStartValue To pEndValue
                        If i <> j And i <> k And i <> l And i <> m And _
                           j <> k And j <> l And j <> m And _
                           k <> l And k <> m And _
                           l <> m Then
                            a = a + 1
                            ReDim Preserve vReturnStrings(a)
                            vReturnStrings(a) = i & "," & j & "," & k & "," & l & "," & m
                        End If
                    Next m
                Next l
            Next k
        Next j
    Next i
    '##### Auflösen String in Array in 2-dimensionales Array
    Dim vReturn, vValues As Variant
    ReDim vReturn(UBound(vReturnStrings), 4)
    For b = 0 To UBound(vReturnStrings)
        vValues = Split(vReturnStrings(b), ",")
        For c = 0 To 4
            vReturn(b, c) = vValues(c)
        Next c
    Next b
    '##### Rückgabe
    getCombinations = vReturn
End Function

'#####################################################################################################
'###### RUN INTCODE-COMPUTER WITH GIVEN PARAMETERS IN LOOP
'######
'###### Führt den Intcode-Computer so oft aus, wie Parameter im Array mitgegeben.
'###### Dabei bekommt der Intcode-Computer als Input(0) den Wert aus dem jeweiligen Parameter mit,
'###### als Input(1) das Result aus dem vorherigen Lauf. Bei ersten Lauf wird Result=0 gesetzt
'######
'###### Parameter #1: pProgramm       Array(0..n) of Numbers (Instructions)
'######                               e.g. 3,15,3,16,1002,16,10,...
'###### Parameter #2: pInputs         Array(0..n) of Phase-Sequence
'######
'###### ReturnValue:      Result of last call IncodeComputer()
'#####################################################################################################
Function runIncodeComputerWithParameters(pProgramm As Variant, pParameters As Variant, pStartValue As Long) As Long
'##### Variablen deklarieren
    Dim i As Integer
    Dim vInputs As Variant
    Dim vReturnValue As Long
    '##### Startwert festlegen
    vReturnValue = pStartValue
    '##### Starte Intcode-Computer mit Programm und Sequence
    For i = 0 To UBound(pParameters)
        vInputs = Array(pParameters(i), vReturnValue)
        vReturnValue = IntcodeComputer(pProgramm, vInputs)
    Next i
    runIncodeComputerWithParameters = vReturnValue
End Function

'#####################################################################################################
'###### INTCODE-COMPUTER
'######
'###### Parameter #1: pProgramm       Array(0..n) of Numbers (Instructions)
'######                               e.g. 3,15,3,16,1002,16,10,...
'###### Parameter #2: pInputs         Array(2) of Phase-Settings
'######                               - array(0) = First Input-Value (from Phase-Setting)
'######                               - array(1) = Second Input-Value (Result from previews Amplifier)
'#####################################################################################################
Function IntcodeComputer(pProgramm As Variant, pInputs As Variant) As Long
    Dim vTargetPos As Long
    Dim vFirstValue As Long
    Dim vSecondValue As Long
    Dim i, y, v As Integer
    v = 0
    Dim vInstruction As String * 5
    For i = 0 To UBound(pProgramm)
        vInstruction = Right("0000" & pProgramm(i), 5)
        y = 0
        If Int(Right(vInstruction, 2)) = 99 Then Exit For
        Select Case (Int(Right(vInstruction, 2)))
            Case 1, 2, 3, 4, 5, 6, 7, 8
                If Mid(vInstruction, 3, 1) = 0 Then vFirstValue = Int(pProgramm(pProgramm(i + 1))) Else vFirstValue = Int(pProgramm(i + 1))
                y = y + 1
        End Select
        Select Case (Int(Right(vInstruction, 2)))
            Case 1, 2, 5, 6, 7, 8
                If Mid(vInstruction, 2, 1) = 0 Then vSecondValue = Int(pProgramm(pProgramm(i + 2))) Else vSecondValue = Int(pProgramm(i + 2))
                y = y + 1
        End Select
        Select Case (Int(Right(vInstruction, 2)))
            Case 1, 2, 7, 8
                If Left(vInstruction, 1) = 0 Then vTargetPos = pProgramm(i + 3) Else MsgBox "ERROR"
                y = y + 1
        End Select
        'Stop
        Select Case (Int(Right(vInstruction, 2)))
            Case 1
                pProgramm(vTargetPos) = CLng(vFirstValue) + vSecondValue
            Case 2
                pProgramm(vTargetPos) = vFirstValue * vSecondValue
            Case 3
                If v < 2 Then
                    pProgramm(pProgramm(i + 1)) = Int(pInputs(v))           'Int(InputBox("Bitte Zahl eingeben:"))
                    v = v + 1
                Else
                    pProgramm(pProgramm(i + 1)) = Int(IntcodeComputer)
                End If
            Case 4
                IntcodeComputer = vFirstValue
                'MsgBox "Ausgabewert ausgeben: " & vFirstValue
            Case 5
                If vFirstValue <> 0 Then i = vSecondValue - 1 - y
            Case 6
                If vFirstValue = 0 Then i = vSecondValue - 1 - y
            Case 7
                If vFirstValue < vSecondValue Then pProgramm(vTargetPos) = 1 Else pProgramm(vTargetPos) = 0
            Case 8
                If vFirstValue = vSecondValue Then pProgramm(vTargetPos) = 1 Else pProgramm(vTargetPos) = 0
            Case Else
                MsgBox "ERROR" & Chr(10) & _
                       "Unknown Instruction" & Chr(10) & _
                       "vValues(" & i & ") = " & pProgramm(i)
                Exit For
        End Select
        i = i + y
    Next i
End Function


Function ArrayToText(pArray As Variant) As String
    Dim vText As String
    Dim i As Integer
    For i = 0 To UBound(pArray)
        vText = vText & Chr(10) & "Array(" & i & ") = " & pArray(i)
    Next
    ArrayToText = vText
End Function
