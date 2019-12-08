'#####################################
'##### Advent of Code
'#####
'##### Day 3: Crossed Wires
'#####################################

Option Explicit
'###########################################################################################
'##### ANZUPASSENDE PARAMETER ##############################################################
'###########################################################################################
'##### Eingabedatei
'Const INPUTFILENAME = "c:\test\input_small.txt"           '-> Result: 6
'Const INPUTFILENAME = "c:\test\input_test1.txt"            '-> Result: 159
'Const INPUTFILENAME = "c:\test\input_test2.txt"            '-> Result:
Const INPUTFILENAME = "c:\test\input_final.txt"            '-> Result: 217
'##### Ausgabedatei, wenn grafische Ausgabe gewünscht (ACHTUNG: Nicht bei großem Feld)
Const CREATEOUPUTFILE = False
Const OUTPUTFILENAME = "c:\test\Output1.txt"
'##### Spielfeldgröße definieren (Quadrat, X*Y)
Const SPIELFELDGROESSE = 20000                              '=> für FINAL = 20000
'###########################################################################################
'##### Festlegung StartPosition (sollte Mittig auf Spielfeld sein
Const STARTPOSWIDTH = SPIELFELDGROESSE / 2
Const STARTPOSHEIGHT = SPIELFELDGROESSE / 2
'##### Spielfeld definieren mit Größe
Dim gField(SPIELFELDGROESSE, SPIELFELDGROESSE) As String
'##### Ergebnis festhalten
Dim gMinimalManhattanDistance As Integer
'##### Eingabezeichenfolge  (2x String, wird in Befehle geschnitten)
Dim gInputCommands1 As String
Dim gInputCommands2 As String
'##### Array, um Überschneidungspunkte zu vermessen array(n,x)
'##### n = Zähler für Überschneidungspunkte, beginnend mit 0 für 1. Überschneidung
'##### x = typ   0 = x-Koordinate
'#####           1 = y-Koordinate
'#####           2 = Steps von 1. Linie         => Dimensionen, anzugeben als Parameter bei Sub-Aufruf
'#####           3 = Steps von 2. Linie
'#####           4 = Summe der Steps von Linie 1 + 2
Dim gListInterceptions(100, 5) As Long
Dim gListInterceptionsCounter As Integer

Sub startProgramm()
    '##### PART ONE
    Erase gField
    Call loadInput
    Call setWire(gInputCommands1, "O")
    Call setWire(gInputCommands2, "#")
    If CREATEOUPUTFILE = True Then Call outputFile
    MsgBox "END PART ONE" & Chr(10) & "gMinimalManhattanDistance=" & gMinimalManhattanDistance
    '##### PART TWO
    gListInterceptionsCounter = 0
    Call listInterceptions
    Call countStepsToInterceptions(gInputCommands1, 2)
    Call countStepsToInterceptions(gInputCommands2, 3)
    Call setSumOfCountSteps
    Call outputInterceptions
    MsgBox "END: File complete"
End Sub


Sub outputInterceptions()
    Open "c:\test\output_interceptions.txt" For Output As #3
    Dim cZeile As String
    Dim z As Integer
    For z = 0 To UBound(gListInterceptions, 1)
        '##### Stoppen, wenn kein Wert mehr vorhanden
        If gListInterceptions(z, 0) = 0 And _
            gListInterceptions(z, 1) = 0 Then
            Exit For
        End If
        cZeile = Right("      " & gListInterceptions(z, 0), 6) & "  " & _
                 Right("      " & gListInterceptions(z, 1), 6) & "  " & _
                 Right("      " & gListInterceptions(z, 2), 6) & "  " & _
                 Right("      " & gListInterceptions(z, 3), 6) & "  " & _
                 Right("      " & gListInterceptions(z, 4), 6)
        
        Write #3, cZeile
        cZeile = ""
    Next
    Close #3
End Sub

Sub loadInput()
    Open INPUTFILENAME For Input As #2
    Line Input #2, gInputCommands1
    Line Input #2, gInputCommands2
    Close #2
End Sub

Sub setWire(pCommands As Variant, pSymbolMark As String)
    Dim vCommands As Variant
    vCommands = Split(pCommands, ",")
    '################################################################
    Dim x As Long
    Dim y As Long
    Dim i As Long
    Dim j As Long
    Dim vCommand As String
    Dim vDistance As Integer
    '##### Start-Punkt in der Mitte
    x = STARTPOSWIDTH
    y = STARTPOSHEIGHT
    gField(x, y) = "S"
    '##### Schleife für Befehlt
    For i = 0 To UBound(vCommands)
        '##### Befehl und Wert auslesen
        vCommand = Left(vCommands(i), 1)
        vDistance = Int(Mid(vCommands(i), 2))
        '##### Ausführen
        For j = 1 To vDistance
            Select Case vCommand
                Case "R"
                    x = x + 1
                Case "L"
                    x = x - 1
                Case "U"
                    y = y - 1
                Case "D"
                    y = y + 1
                Case Else
                    MsgBox "ERROR SELECT cCommand"
            End Select
            If checkCrossingLines(x, y, pSymbolMark) = False Then
                gField(x, y) = pSymbolMark
            Else
                gField(x, y) = "X"
            End If
        Next
        gField(x, y) = pSymbolMark
    Next
End Sub

Sub outputFile()
    Open OUTPUTFILENAME For Output As #1
    Dim cZeile As String
    Dim i As Long
    Dim j As Long
    For j = 0 To UBound(gField, 1)
        For i = 0 To UBound(gField, 2)
            If gField(i, j) = "" Then
                gField(i, j) = "."
            End If
            cZeile = cZeile & gField(i, j)
        Next
        Write #1, cZeile
        cZeile = ""
    Next
    Close #1
End Sub

Function checkCrossingLines(x As Long, y As Long, pSymbolMark As String) As Boolean
    Dim vSum As Integer
    Dim DiffX As Long
    Dim DiffY As Long
    If gField(x, y) <> "" And gField(x, y) <> pSymbolMark Then
        '##### Differenz ermitteln
        DiffX = STARTPOSWIDTH - x
        If DiffX < 0 Then DiffX = DiffX * -1
        DiffY = STARTPOSHEIGHT - y
        If DiffY < 0 Then DiffY = DiffY * -1
        '#####
        vSum = DiffX + DiffY
        If gMinimalManhattanDistance = 0 Or gMinimalManhattanDistance > vSum Then
            'MsgBox "checkCrossingLines(" & x & "," & y & ")" & Chr(10) & _
                   "DiffX = " & DiffX & Chr(10) & _
                   "DiffY = " & DiffY & Chr(10) & _
                   "gMinimalManhattanDistance = " & gMinimalManhattanDistance & Chr(10) & _
                   "vSum = " & vSum
            gMinimalManhattanDistance = vSum
        End If
        checkCrossingLines = True
    Else
        checkCrossingLines = False
    End If
End Function

Sub listInterceptions()
    Dim x As Integer
    Dim y As Integer
    For x = 0 To SPIELFELDGROESSE
        For y = 0 To SPIELFELDGROESSE
            If gField(x, y) = "X" Then
                gListInterceptions(gListInterceptionsCounter, 0) = x
                gListInterceptions(gListInterceptionsCounter, 1) = y
                gListInterceptionsCounter = gListInterceptionsCounter + 1
            End If
        Next
    Next
End Sub

Sub countStepsToInterceptions(pCommands As String, gDimensions As Integer)
    Dim vCommands As Variant
    vCommands = Split(pCommands, ",")
    '################################################################
    Dim x As Long
    Dim y As Long
    Dim i As Long
    Dim j As Long
    Dim z As Integer
    Dim vCommand As String
    Dim vDistance As Integer
    '##### Schritte für Rückgabewert zählen
    Dim vCounter As Long
    vCounter = 0
    '##### Start-Punkt in der Mitte
    x = STARTPOSWIDTH
    y = STARTPOSHEIGHT
    If gField(x, y) <> "S" Then
        MsgBox "ERROR: Startpunkt nicht gefunden"
        End
    End If
    '##### Schleife für Befehlt
    For i = 0 To UBound(vCommands)
        '##### Befehl und Wert auslesen
        vCommand = Left(vCommands(i), 1)
        vDistance = Int(Mid(vCommands(i), 2))
        '##### Ausführen
        For j = 1 To vDistance
            Select Case vCommand
                Case "R"
                    x = x + 1
                Case "L"
                    x = x - 1
                Case "U"
                    y = y - 1
                Case "D"
                    y = y + 1
                Case Else
                    MsgBox "ERROR SELECT cCommand"
            End Select
            vCounter = vCounter + 1
            If gField(x, y) = "X" Then
                '##### Finde Koordinate in InterceptionList
                For z = 0 To UBound(gListInterceptions, 1)
                    If gListInterceptions(z, 0) = x And _
                       gListInterceptions(z, 1) = y Then
                        gListInterceptions(z, gDimensions) = vCounter
                    End If
                Next
            End If
        Next
    Next
End Sub

Sub setSumOfCountSteps()
    Dim z As Integer
    For z = 0 To UBound(gListInterceptions)
        '##### Summieren WegStrecke
        gListInterceptions(z, 4) = gListInterceptions(z, 2) + gListInterceptions(z, 3)
    Next
End Sub
