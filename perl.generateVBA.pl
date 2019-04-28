#!/bin/perl



for ($i=5;$i<=10000;$i++ ){

print " 

Calculate
Range(\"K6\").Select
    Selection.Copy 
    Range(\"N",$i,"\").Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    Application.CutCopyMode = False
    
    Range(\"K5\").Select
    Selection.Copy
    Range(\"O",$i,"\").Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    Application.CutCopyMode = False
    
    
    Range(\"K4\").Select
    Selection.Copy
    Range(\"P",$i,"\").Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False \n";

}   
