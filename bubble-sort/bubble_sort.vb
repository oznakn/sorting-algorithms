Module Module1

    Sub Main()
        Dim items As New List(Of Integer)(New Integer() {1, 5, 13, 36, 2, 1000, 23})

        Dim is_sorted As Boolean = False
        Dim temp As Integer

        While Not is_sorted
            is_sorted = True
            For i = 0 To items.Count - 2
                If items(i) > items(i + 1) Then
                    temp = items(i)
                    items(i) = items(i + 1)
                    items(i + 1) = temp
                    is_sorted = False
                End If
            Next
        End While

        For Each i In items
            Console.Write("{0}, ", i)
        Next
    End Sub

End Module
