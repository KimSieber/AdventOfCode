Option Explicit
'#####################################
'##### Advent of Code
'#####
'##### Day 8: Space Image Format
'#####################################
Const INPUTFILENAME = "C:\test\input.txt"
Const OUPUTFILENAME = "C:\test\output.txt"
Dim gPics(100, 6, 25) As Byte
Dim gPic(6, 25) As Byte

Sub start()
    Dim vInput As Variant
    Call loadInput
    Dim vLayerMin As Byte
    vLayerMin = getLayerWithMinZero()
    Dim vCountOneAndTwo As Variant
    vCountOneAndTwo = getCountOneAndTwo(vLayerMin)
    Dim vResult As Long
    vResult = multiplicateNumbers(vCountOneAndTwo(0), vCountOneAndTwo(1))
    MsgBox "vResult=" & vResult
    '######################################
    '##### PART TWO
    '######################################
    Call initilizePic
    Call createPic
    Call printOutputFile(gPic)
    MsgBox "ready."
End Sub

'##### Einlesen der Daten in 3-dimensionales Array
Sub loadInput()
    Dim vInput As Variant
    ReDim vInput(1, 1)
    Open INPUTFILENAME For Input As #1
    Dim i, j, k As Integer
    For i = 0 To 99            '##### Layer
        For j = 0 To 5         '##### Rows
            For k = 0 To 24    '##### Columns
                gPics(i, j, k) = Input(1, #1)
            Next k
        Next j
    Next i
    Close #1
End Sub

'##### Ermitteln der Ebene mit den wenigsten 0-Stellen
Function getLayerWithMinZero() As Byte
    Dim vLayer, vLayerZero, actZero As Byte
    vLayer = 0
    vLayerZero = 150
    Dim i, j, k As Integer
    For i = 0 To 99            '##### Layer
        actZero = 0
        For j = 0 To 5         '##### Rows
            For k = 0 To 24    '##### Columns
                If gPics(i, j, k) = 0 Then actZero = actZero + 1
            Next k
        Next j
        If actZero < vLayerZero Then
            vLayerZero = actZero
            vLayer = i
        End If
    Next i
    getLayerWithMinZero = vLayer
    'MsgBox "vLayerZero=" & vLayerZero & Chr(10) & "vLayer=" & vLayer
End Function

'##### Anzahl der 1er und 2er in dieser Ebene zählen
Function getCountOneAndTwo(pLayer As Byte) As Variant
    Dim vCountOneAndTwo(2) As Byte
    vCountOneAndTwo(0) = 0
    vCountOneAndTwo(1) = 0
    Dim j, k As Integer
    For j = 0 To 5         '##### Rows
        For k = 0 To 24    '##### Columns
            If gPics(pLayer, j, k) = 1 Then vCountOneAndTwo(0) = vCountOneAndTwo(0) + 1
            If gPics(pLayer, j, k) = 2 Then vCountOneAndTwo(1) = vCountOneAndTwo(1) + 1
        Next k
    Next j
    'MsgBox "vCountOneAndTwo(n)=" & vCountOneAndTwo(0) & ":" & vCountOneAndTwo(1)
    getCountOneAndTwo = vCountOneAndTwo
End Function


'##### Multiplikation er beiden Anzahlen und Ergebnis ausgeben
Function multiplicateNumbers(pNumber1 As Variant, pNumber2 As Variant) As Long
    multiplicateNumbers = pNumber1 * pNumber2
End Function

'######################################
'##### PART TWO
'######################################
Sub initilizePic()         '##### -> Alles auf 2=transparent setzen
    Dim j, k As Integer
    For j = 0 To 5         '##### Rows
        For k = 0 To 24    '##### Columns
            gPic(j, k) = 2
        Next k
    Next j
End Sub

Sub createPic()
    Dim i, j, k As Integer
    For i = 0 To 99            '##### Layer
        For j = 0 To 5         '##### Rows
            For k = 0 To 24    '##### Columns
                If gPic(j, k) = 2 Then
                    gPic(j, k) = gPics(i, j, k)
                End If
            Next k
        Next j
    Next i
End Sub

Sub printOutputFile(pArray As Variant)
    Open OUPUTFILENAME For Output As #1
    Dim vLine, vChar As String
    Dim j, k As Integer
    For j = 0 To 5         '##### Rows
        vLine = ""
        For k = 0 To 24    '##### Columns
            If gPic(j, k) = 1 Then vChar = "*" Else vChar = " "
            vLine = vLine & vChar
        Next k
        Print #1, vLine
    Next j
    Close #1
End Sub
