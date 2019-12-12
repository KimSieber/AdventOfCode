Option Explicit
'#####################################
'##### Advent of Code
'#####
'##### Day 6: Universal Orbit Map
'#####################################
Const INPUTFILENAME = "C:\test\input.txt"              '-> universelle INPUT-Liste
'Const INPUTFILENAME = "C:\test\inputtest.txt"          '-> TEST für PART ONE
'Const INPUTFILENAME = "C:\test\inputtest2.txt"         '-> TEST für PART TWO

Sub start()
    '##### Input-Daten laden in Array
    Dim vOrbits() As Variant
    vOrbits = loadOrbits
    '###########################################################
    '##### PART ONE
    '#####
    '##### Anzahl Orbits ermitteln über alles
    '###########################################################
    '##### Liste aller Objekte erzeugen (redundanzfrei)
    Dim vObjects() As Variant
    vObjects = getObjectList(vOrbits)
    '###### Orbits je Objekt zählen und in zweidimensionales Array setzen
    '###### vObjectList(n,z)   n   = Objekt-Zähler
    '######                    z=0 = Objektname
    '######                    z=1 = Anzahl Orbits
    Dim vObjectList() As Variant
    ReDim vObjectList(UBound(vObjects) + 1, 2)
    Dim i, vCounter As Integer
    Dim vSumCounter As Long
    vSumCounter = 0
    For i = 0 To UBound(vObjects)
        vObjectList(i, 0) = vObjects(i)
        vCounter = countOrbits(vObjects(i), vOrbits)
        vObjectList(i, 1) = vCounter
        vSumCounter = vSumCounter + vCounter
    Next i
    '##### Anzahlen ausgeben (Kontrolle)
    'MsgBox "UBound(vOrbits, 1)=" & UBound(vOrbits, 1) + 1
    'MsgBox "UBound(vObjects)=" & UBound(vObjects) + 1
    '##### Kontrollausgaben (nur bei kleiner Test-Input-Datei)
    'Call MsgBoxArra2Dimensions("Orbits", vOrbits)
    'Call MsgBoxArray1Dimension("Objects", vObjects)
    '##### Orbits zählen (Ergebnis)
    MsgBox "Anzahl Orbits (vSumCounter)=" & vSumCounter
    
    '###########################################################
    '##### PART TWO
    '#####
    '##### Weg von YOU to SAN ermitteln
    '###########################################################
    Dim vWaysFrom() As Variant
    vWaysFrom = investigateWayFromYouToSan(vOrbits)
    MsgBox "FERTIG !!! " & Chr(10) & _
           "Weg von YOU zum gemeinsamen Schnittpunkt = " & vWaysFrom(0) & Chr(10) & _
           "Weg von SAN zum gemeinsamen Schnittpunkt = " & vWaysFrom(1) & Chr(10) & _
           Chr(10) & _
           "Ergebnis ist somit: " & (vWaysFrom(0) + vWaysFrom(1))
End Sub

Function investigateWayFromYouToSan(pOrbits As Variant) As Variant()
    '##### Liste YOU erstellen
    Dim vListObjectsYOU() As Variant
    vListObjectsYOU = getLowerOrbitList("YOU", pOrbits)
    '##### Liste YOU erstellen
    Dim vListObjectsSAN() As Variant
    vListObjectsSAN = getLowerOrbitList("SAN", pOrbits)
    
    Call MsgBoxArray1Dimension("List Objekte von YOU zu COM: ", vListObjectsYOU)
    Call MsgBoxArray1Dimension("List Objekte von SAN zu COM: ", vListObjectsSAN)
    '##### Vergleiche Strecken auf erste Gemeinsamkeit
    Dim i, j As Integer
    For i = 0 To UBound(vListObjectsYOU)
        j = getPositionOfObjectInList(vListObjectsYOU(i), vListObjectsSAN)
        If j > 0 Then Exit For
    Next i
    Dim vResult(1) As Variant
    vResult(0) = i
    vResult(1) = j
    investigateWayFromYouToSan = vResult
End Function

Function getPositionOfObjectInList(pObject As Variant, pListObjects As Variant) As Integer
    Dim i As Integer
    For i = 0 To UBound(pListObjects)
        If pListObjects(i) = pObject Then
            getPositionOfObjectInList = i
            Exit Function
        End If
    Next i
    getPositionOfObjectInList = 0
End Function

Function getLowerOrbitList(pStartObject As Variant, pOrbits As Variant) As Variant()
    Dim vListObjects() As Variant
    Dim z As Integer
    z = 0
    Dim vActOrbit As String
    vActOrbit = getLowerOrbit(pStartObject, pOrbits)
    ReDim vListObjects(z)
    vListObjects(z) = vActOrbit
    Do While vActOrbit <> "COM"
        vActOrbit = getLowerOrbit(vListObjects(z), pOrbits)
        z = z + 1
        ReDim Preserve vListObjects(z)
        vListObjects(z) = vActOrbit
    Loop
    getLowerOrbitList = vListObjects
End Function


Function getLowerOrbit(pObject As Variant, pOrbits As Variant) As String
    Dim i As Integer
    For i = 0 To UBound(pOrbits, 1)
        If pOrbits(i, 1) = pObject Then
            getLowerOrbit = pOrbits(i, 0)
        End If
    Next i
End Function

Function countOrbits(pObject As Variant, pOrbits As Variant) As Long
    countOrbits = 0
    If pObject = "COM" Then Exit Function
    Dim i As Integer
    For i = 0 To UBound(pOrbits)
        If pOrbits(i, 1) = pObject Then
            '##### rekursiver Aufruf, bis Wurzel (=COM) erreicht)
            countOrbits = countOrbits + 1 + countOrbits(pOrbits(i, 0), pOrbits)
        End If
    Next i
End Function

Function getObjectList(pOrbits() As Variant) As Variant()
    Dim i, j, n, z As Integer
    z = -1
    Dim vObjectList() As Variant
    ReDim Preserve vObjectList(1)
    Dim vNewValue As Boolean
    For n = 0 To 1
        For i = 0 To UBound(pOrbits, 1)
            vNewValue = True
            For j = 0 To UBound(vObjectList)
                If pOrbits(i, n) = vObjectList(j) Then
                    vNewValue = False
                    Exit For
                End If
            Next
            If vNewValue = True Then
                z = z + 1
                ReDim Preserve vObjectList(z)
                vObjectList(z) = pOrbits(i, n)
            End If
        Next i
    Next n
    getObjectList = vObjectList
End Function

Function loadOrbits() As Variant()
    Dim i, j As Integer
    i = -1
    Dim vLine As String
    Dim vOrbit As Variant
    Dim vOrbitList() As Variant
    Close #1
    Open INPUTFILENAME For Input As #1
    Do While Not EOF(1)
        i = i + 1
        Line Input #1, vLine
        ReDim Preserve vOrbitList(i)
        vOrbitList(i) = vLine
    Loop
    Close #1
    Dim vOrbits() As Variant
    ReDim vOrbits(i, 2)
    For j = 0 To i
        vOrbit = Split(vOrbitList(j), ")")
        vOrbits(j, 0) = vOrbit(0)
        vOrbits(j, 1) = vOrbit(1)
    Next j
    loadOrbits = vOrbits
End Function


'#################################################
'##### Ausgabe-Prozeduren nur für Test-Zwecke
'#################################################
Sub MsgBoxArray1Dimension(pText As String, pValues As Variant)
    Dim vText As String
    Dim i As Integer
    For i = 0 To UBound(pValues)
        vText = vText & Chr(10) & pText & " " & Right("000" & i, 4) & " - " & pValues(i)
    Next
    MsgBox vText
End Sub

Sub MsgBoxArra2Dimensions(pText As String, pValues As Variant)
    Dim vText As String
    Dim i As Integer
    For i = 0 To UBound(pValues, 1)
        vText = vText & Chr(10) & pText & " " & Right("000" & i, 4) & " - " & pValues(i, 0) & " ) " & pValues(i, 1)
    Next
    MsgBox vText
End Sub
