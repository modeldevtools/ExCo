
# -*- coding: utf-8 -*-

"""
    Ex.Co. LICENSE :
        This file is part of Ex.Co..

        Ex.Co. is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        Ex.Co. is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with Ex.Co..  If not, see <http://www.gnu.org/licenses/>.


    PYTHON LICENSE :
        "Python" and the Python logos are trademarks or registered trademarks of the Python Software Foundation,
        used by Ex.Co. with permission from the Foundation


    Cython LICENSE:
        Cython is freely available under the open source Apache License


    PyQt4 LICENSE :
        PyQt4 is licensed under the GNU General Public License version 3
    PyQt Alternative Logo LICENSE:
        The PyQt Alternative Logo is licensed under Creative Commons CC0 1.0 Universal Public Domain Dedication


    Qt Logo LICENSE:
        The Qt logo is copyright of Digia Plc and/or its subsidiaries.
        Digia, Qt and their respective logos are trademarks of Digia Corporation in Finland and/or other countries worldwide.


    Tango Icons LICENSE:
        The Tango base icon theme is released to the Public Domain.
        The Tango base icon theme is made possible by the Tango Desktop Project.
    
    My Tango Style Icons LICENSE:
        The Tango icons I created are released under the GNU General Public License version 3.
    
    
    Eric6 LICENSE:
        Eric6 IDE is licensed under the GNU General Public License version 3


    Nuitka LICENSE:
        Nuitka is a Python compiler compatible with Ex.Co..
        Nuitka is freely available under the open source Apache License.
"""

##  FILE DESCRIPTION:
##      Earth theme

import PyQt4.QtGui


Form = "#585a55"
Cursor = PyQt4.QtGui.QColor(0xff, 0xff, 0xff)


class FoldMargin:
    ForeGround = PyQt4.QtGui.QColor(0xffffffff)
    BackGround = PyQt4.QtGui.QColor(0xff2e3436)


class LineMargin:
    ForeGround = PyQt4.QtGui.QColor(0xffffffff)
    BackGround = PyQt4.QtGui.QColor(0xff2e3436)


class Indication:
    Font = "#e6e6e6"
    ActiveBackGround = "#1a0f0b"
    ActiveBorder = "#e6e6e6"
    PassiveBackGround = "#585a55"
    PassiveBorder = "#b3935c"

    
class Font:
    Default = PyQt4.QtGui.QColor(0xffc3be98)
    
    class Ada:
        Default = 0xffc3be98
        Comment = 0xff679d47
        Keyword = 0xff519872
        String = 0xff7ca563
        Procedure = 0xffb3935c
        Number = 0xff6c9686
        Type = 0xff519872
        Package = 0xffe1aa7d
    
    class Nim:
        Default = 0xffc3be98
        Comment = 0xff679d47
        BasicKeyword = 0xff519872
        TopKeyword = 0xff407fc0
        String = 0xff7ca563
        LongString = 0xffe1aa7d
        Number = 0xff6c9686
        Operator = 0xff7f7f7f
        Unsafe = 0xffc00000
        Type = 0xff6e6e00
        DocumentationComment = 0xff7f0a0a
        Definition = 0xff6c9686
        Class = 0xffb3935c
        KeywordOperator = 0xff963cc8
        CharLiteral = 0xff00c8ff
        CaseOf = 0xff8000ff
        UserKeyword = 0xffff8040
        MultilineComment = 0xff006c6c
        MultilineDocumentation = 0xff6e3296
        Pragma = 0xffc07f40
    
    class Oberon:
        Default = 0xffc3be98
        Comment = 0xff679d47
        Keyword = 0xff519872
        String = 0xff7ca563
        Procedure = 0xffb3935c
        Module = 0xffe1aa7d
        Number = 0xff6c9686
        Type = 0xff519872
    
    
    # Generated
    class AVS:
        BlockComment = 0xff679d47
        ClipProperty = 0xff519872
        Default = 0xffc3be98
        Filter = 0xff519872
        Function = 0xff6c9686
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        KeywordSet6 = 0xff8000ff
        LineComment = 0xff679d47
        NestedBlockComment = 0xff679d47
        Number = 0xff6c9686
        Operator = 0xffc3be98
        Plugin = 0xff0080c0
        String = 0xff7ca563
        TripleString = 0xff7ca563
    
    class Bash:
        Backticks = 0xffffff00
        Comment = 0xff679d47
        Default = 0xff808080
        DoubleQuotedString = 0xff7ca563
        Error = 0xffffff00
        HereDocumentDelimiter = 0xffc3be98
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        Number = 0xff6c9686
        Operator = 0xffc3be98
        ParameterExpansion = 0xffc3be98
        Scalar = 0xffc3be98
        SingleQuotedHereDocument = 0xff7ca563
        SingleQuotedString = 0xff7ca563
    
    class Batch:
        Comment = 0xff679d47
        Default = 0xffc3be98
        ExternalCommand = 0xff519872
        HideCommandChar = 0xff7f7f00
        Keyword = 0xff519872
        Label = 0xff7ca563
        Operator = 0xffc3be98
        Variable = 0xff800080
    
    class CMake:
        BlockForeach = 0xff519872
        BlockIf = 0xff519872
        BlockMacro = 0xff519872
        BlockWhile = 0xff519872
        Comment = 0xff679d47
        Default = 0xffc3be98
        Function = 0xff519872
        KeywordSet3 = 0xffc3be98
        Label = 0xffcc3300
        Number = 0xff6c9686
        String = 0xff7ca563
        StringLeftQuote = 0xff7ca563
        StringRightQuote = 0xff7ca563
        StringVariable = 0xffcc3300
        Variable = 0xff800000
    
    class CPP:
        Comment = 0xff679d47
        CommentDoc = 0xff3f703f
        CommentDocKeyword = 0xff3060a0
        CommentDocKeywordError = 0xff804020
        CommentLine = 0xff679d47
        CommentLineDoc = 0xff3f703f
        Default = 0xff808080
        DoubleQuotedString = 0xff7ca563
        GlobalClass = 0xffc3be98
        HashQuotedString = 0xff679d47
        Identifier = 0xffc3be98
        InactiveComment = 0xff90b090
        InactiveCommentDoc = 0xffd0d0d0
        InactiveCommentDocKeyword = 0xffc0c0c0
        InactiveCommentDocKeywordError = 0xffc0c0c0
        InactiveCommentLine = 0xff90b090
        InactiveCommentLineDoc = 0xffc0c0c0
        InactiveDefault = 0xffc0c0c0
        InactiveDoubleQuotedString = 0xffb090b0
        InactiveGlobalClass = 0xffb0b0b0
        InactiveHashQuotedString = 0xffc3be98
        InactiveIdentifier = 0xffb0b0b0
        InactiveKeyword = 0xff9090b0
        InactiveKeywordSet2 = 0xffc0c0c0
        InactiveNumber = 0xff90b090
        InactiveOperator = 0xffb0b0b0
        InactivePreProcessor = 0xffb0b090
        InactivePreProcessorComment = 0xff1a0f0b
        InactivePreProcessorCommentLineDoc = 0xffc0c0c0
        InactiveRawString = 0xffc3be98
        InactiveRegex = 0xff7faf7f
        InactiveSingleQuotedString = 0xffb090b0
        InactiveTripleQuotedVerbatimString = 0xffc3be98
        InactiveUUID = 0xffc0c0c0
        InactiveUnclosedString = 0xffc3be98
        InactiveVerbatimString = 0xff90b090
        Keyword = 0xff519872
        KeywordSet2 = 0xffc3be98
        Number = 0xff6c9686
        Operator = 0xffc3be98
        PreProcessor = 0xff7f7f00
        PreProcessorComment = 0xff659900
        PreProcessorCommentLineDoc = 0xff3f703f
        RawString = 0xff7ca563
        Regex = 0xff3f7f3f
        SingleQuotedString = 0xff7ca563
        TripleQuotedVerbatimString = 0xff679d47
        UUID = 0xffc3be98
        UnclosedString = 0xffc3be98
        VerbatimString = 0xff679d47
    
    class CSS:
        AtRule = 0xff7f7f00
        Attribute = 0xff800000
        CSS1Property = 0xff0040e0
        CSS2Property = 0xff00a0e0
        CSS3Property = 0xffc3be98
        ClassSelector = 0xffc3be98
        Comment = 0xff679d47
        Default = 0xffff0080
        DoubleQuotedString = 0xff7ca563
        ExtendedCSSProperty = 0xffc3be98
        ExtendedPseudoClass = 0xffc3be98
        ExtendedPseudoElement = 0xffc3be98
        IDSelector = 0xff6c9686
        Important = 0xffff8000
        MediaRule = 0xff7f7f00
        Operator = 0xffc3be98
        PseudoClass = 0xff800000
        PseudoElement = 0xffc3be98
        SingleQuotedString = 0xff7ca563
        Tag = 0xff519872
        UnknownProperty = 0xffff0000
        UnknownPseudoClass = 0xffff0000
        Value = 0xff7ca563
        Variable = 0xffc3be98
    
    class CSharp:
        Comment = 0xff679d47
        CommentDoc = 0xff3f703f
        CommentDocKeyword = 0xff3060a0
        CommentDocKeywordError = 0xff804020
        CommentLine = 0xff679d47
        CommentLineDoc = 0xff3f703f
        Default = 0xff808080
        DoubleQuotedString = 0xff7ca563
        GlobalClass = 0xffc3be98
        HashQuotedString = 0xff679d47
        Identifier = 0xffc3be98
        InactiveComment = 0xff90b090
        InactiveCommentDoc = 0xffd0d0d0
        InactiveCommentDocKeyword = 0xffc0c0c0
        InactiveCommentDocKeywordError = 0xffc0c0c0
        InactiveCommentLine = 0xff90b090
        InactiveCommentLineDoc = 0xffc0c0c0
        InactiveDefault = 0xffc0c0c0
        InactiveDoubleQuotedString = 0xffb090b0
        InactiveGlobalClass = 0xffb0b0b0
        InactiveHashQuotedString = 0xffc3be98
        InactiveIdentifier = 0xffb0b0b0
        InactiveKeyword = 0xff9090b0
        InactiveKeywordSet2 = 0xffc0c0c0
        InactiveNumber = 0xff90b090
        InactiveOperator = 0xffb0b0b0
        InactivePreProcessor = 0xffb0b090
        InactivePreProcessorComment = 0xff1a0f0b
        InactivePreProcessorCommentLineDoc = 0xffc0c0c0
        InactiveRawString = 0xffc3be98
        InactiveRegex = 0xff7faf7f
        InactiveSingleQuotedString = 0xffb090b0
        InactiveTripleQuotedVerbatimString = 0xffc3be98
        InactiveUUID = 0xffc0c0c0
        InactiveUnclosedString = 0xffc3be98
        InactiveVerbatimString = 0xff90b090
        Keyword = 0xff519872
        KeywordSet2 = 0xffc3be98
        Number = 0xff6c9686
        Operator = 0xffc3be98
        PreProcessor = 0xff7f7f00
        PreProcessorComment = 0xff659900
        PreProcessorCommentLineDoc = 0xff3f703f
        RawString = 0xff7ca563
        Regex = 0xff3f7f3f
        SingleQuotedString = 0xff7ca563
        TripleQuotedVerbatimString = 0xff679d47
        UUID = 0xffc3be98
        UnclosedString = 0xffc3be98
        VerbatimString = 0xff679d47
    
    class CoffeeScript:
        BlockRegex = 0xff3f7f3f
        BlockRegexComment = 0xff679d47
        Comment = 0xff679d47
        CommentBlock = 0xff679d47
        CommentDoc = 0xff3f703f
        CommentDocKeyword = 0xff3060a0
        CommentDocKeywordError = 0xff804020
        CommentLine = 0xff679d47
        CommentLineDoc = 0xff3f703f
        Default = 0xff808080
        DoubleQuotedString = 0xff7ca563
        GlobalClass = 0xffc3be98
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        KeywordSet2 = 0xffc3be98
        Number = 0xff6c9686
        Operator = 0xffc3be98
        PreProcessor = 0xff7f7f00
        Regex = 0xff3f7f3f
        SingleQuotedString = 0xff7ca563
        UUID = 0xffc3be98
        UnclosedString = 0xffc3be98
        VerbatimString = 0xff679d47
    
    class D:
        BackquoteString = 0xffc3be98
        Character = 0xff7ca563
        Comment = 0xff679d47
        CommentDoc = 0xff3f703f
        CommentDocKeyword = 0xff3060a0
        CommentDocKeywordError = 0xff804020
        CommentLine = 0xff679d47
        CommentLineDoc = 0xff3f703f
        CommentNested = 0xffa0c0a0
        Default = 0xff808080
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        KeywordDoc = 0xff519872
        KeywordSecondary = 0xff519872
        KeywordSet5 = 0xffc3be98
        KeywordSet6 = 0xffc3be98
        KeywordSet7 = 0xffc3be98
        Number = 0xff6c9686
        Operator = 0xffc3be98
        RawString = 0xffc3be98
        String = 0xff7ca563
        Typedefs = 0xff519872
        UnclosedString = 0xffc3be98
    
    class Diff:
        Command = 0xff7f7f00
        Comment = 0xff679d47
        Default = 0xffc3be98
        Header = 0xffe1aa7d
        LineAdded = 0xff519872
        LineChanged = 0xff7f7f7f
        LineRemoved = 0xff6c9686
        Position = 0xff7ca563
    
    class Fortran:
        Comment = 0xff679d47
        Continuation = 0xffc3be98
        Default = 0xff808080
        DottedOperator = 0xffc3be98
        DoubleQuotedString = 0xff7ca563
        ExtendedFunction = 0xffb04080
        Identifier = 0xffc3be98
        IntrinsicFunction = 0xffb00040
        Keyword = 0xff519872
        Label = 0xffe0c0e0
        Number = 0xff6c9686
        Operator = 0xffc3be98
        PreProcessor = 0xff7f7f00
        SingleQuotedString = 0xff7ca563
        UnclosedString = 0xffc3be98
    
    class Fortran77:
        Comment = 0xff679d47
        Continuation = 0xffc3be98
        Default = 0xff808080
        DottedOperator = 0xffc3be98
        DoubleQuotedString = 0xff7ca563
        ExtendedFunction = 0xffb04080
        Identifier = 0xffc3be98
        IntrinsicFunction = 0xffb00040
        Keyword = 0xff519872
        Label = 0xffe0c0e0
        Number = 0xff6c9686
        Operator = 0xffc3be98
        PreProcessor = 0xff7f7f00
        SingleQuotedString = 0xff7ca563
        UnclosedString = 0xffc3be98
    
    class HTML:
        ASPAtStart = 0xffc3be98
        ASPJavaScriptComment = 0xff679d47
        ASPJavaScriptCommentDoc = 0xff7f7f7f
        ASPJavaScriptCommentLine = 0xff679d47
        ASPJavaScriptDefault = 0xffc3be98
        ASPJavaScriptDoubleQuotedString = 0xff7ca563
        ASPJavaScriptKeyword = 0xff519872
        ASPJavaScriptNumber = 0xff6c9686
        ASPJavaScriptRegex = 0xffc3be98
        ASPJavaScriptSingleQuotedString = 0xff7ca563
        ASPJavaScriptStart = 0xff7f7f00
        ASPJavaScriptSymbol = 0xffc3be98
        ASPJavaScriptUnclosedString = 0xffc3be98
        ASPJavaScriptWord = 0xffc3be98
        ASPPythonClassName = 0xffb3935c
        ASPPythonComment = 0xff679d47
        ASPPythonDefault = 0xff808080
        ASPPythonDoubleQuotedString = 0xff7ca563
        ASPPythonFunctionMethodName = 0xff6c9686
        ASPPythonIdentifier = 0xffc3be98
        ASPPythonKeyword = 0xff519872
        ASPPythonNumber = 0xff6c9686
        ASPPythonOperator = 0xffc3be98
        ASPPythonSingleQuotedString = 0xff7ca563
        ASPPythonStart = 0xff808080
        ASPPythonTripleDoubleQuotedString = 0xffe1aa7d
        ASPPythonTripleSingleQuotedString = 0xffe1aa7d
        ASPStart = 0xffc3be98
        ASPVBScriptComment = 0xff008000
        ASPVBScriptDefault = 0xffc3be98
        ASPVBScriptIdentifier = 0xff007fff
        ASPVBScriptKeyword = 0xff007fff
        ASPVBScriptNumber = 0xff008080
        ASPVBScriptStart = 0xffc3be98
        ASPVBScriptString = 0xff800080
        ASPVBScriptUnclosedString = 0xff007fff
        ASPXCComment = 0xff1a0f0b
        Attribute = 0xff008080
        CDATA = 0xffc3be98
        Default = 0xffc3be98
        Entity = 0xff800080
        HTMLComment = 0xff808000
        HTMLDoubleQuotedString = 0xff7ca563
        HTMLNumber = 0xff6c9686
        HTMLSingleQuotedString = 0xff7ca563
        HTMLValue = 0xffff00ff
        JavaScriptComment = 0xff679d47
        JavaScriptCommentDoc = 0xff3f703f
        JavaScriptCommentLine = 0xff679d47
        JavaScriptDefault = 0xffc3be98
        JavaScriptDoubleQuotedString = 0xff7ca563
        JavaScriptKeyword = 0xff519872
        JavaScriptNumber = 0xff6c9686
        JavaScriptRegex = 0xffc3be98
        JavaScriptSingleQuotedString = 0xff7ca563
        JavaScriptStart = 0xff7f7f00
        JavaScriptSymbol = 0xffc3be98
        JavaScriptUnclosedString = 0xffc3be98
        JavaScriptWord = 0xffc3be98
        OtherInTag = 0xff800080
        PHPComment = 0xff999999
        PHPCommentLine = 0xff666666
        PHPDefault = 0xff000033
        PHPDoubleQuotedString = 0xff679d47
        PHPDoubleQuotedVariable = 0xff519872
        PHPKeyword = 0xff7ca563
        PHPNumber = 0xffcc9900
        PHPOperator = 0xffc3be98
        PHPSingleQuotedString = 0xff009f00
        PHPStart = 0xffb3935c
        PHPVariable = 0xff519872
        PythonClassName = 0xffb3935c
        PythonComment = 0xff679d47
        PythonDefault = 0xff808080
        PythonDoubleQuotedString = 0xff7ca563
        PythonFunctionMethodName = 0xff6c9686
        PythonIdentifier = 0xffc3be98
        PythonKeyword = 0xff519872
        PythonNumber = 0xff6c9686
        PythonOperator = 0xffc3be98
        PythonSingleQuotedString = 0xff7ca563
        PythonStart = 0xff808080
        PythonTripleDoubleQuotedString = 0xffe1aa7d
        PythonTripleSingleQuotedString = 0xffe1aa7d
        SGMLBlockDefault = 0xff000066
        SGMLCommand = 0xff007fff
        SGMLComment = 0xff808000
        SGMLDefault = 0xff007fff
        SGMLDoubleQuotedString = 0xff800000
        SGMLEntity = 0xff333333
        SGMLError = 0xff800000
        SGMLParameter = 0xff006600
        SGMLParameterComment = 0xff1a0f0b
        SGMLSingleQuotedString = 0xff993300
        SGMLSpecial = 0xff3366ff
        Script = 0xff007fff
        Tag = 0xff007fff
        UnknownAttribute = 0xffff0000
        UnknownTag = 0xffff0000
        VBScriptComment = 0xff008000
        VBScriptDefault = 0xffc3be98
        VBScriptIdentifier = 0xff007fff
        VBScriptKeyword = 0xff007fff
        VBScriptNumber = 0xff008080
        VBScriptStart = 0xffc3be98
        VBScriptString = 0xff800080
        VBScriptUnclosedString = 0xff007fff
        XMLEnd = 0xffb3935c
        XMLStart = 0xffb3935c
        XMLTagEnd = 0xff007fff
    
    class IDL:
        Comment = 0xff679d47
        CommentDoc = 0xff3f703f
        CommentDocKeyword = 0xff3060a0
        CommentDocKeywordError = 0xff804020
        CommentLine = 0xff679d47
        CommentLineDoc = 0xff3f703f
        Default = 0xff808080
        DoubleQuotedString = 0xff7ca563
        GlobalClass = 0xffc3be98
        HashQuotedString = 0xff679d47
        Identifier = 0xffc3be98
        InactiveComment = 0xff90b090
        InactiveCommentDoc = 0xffd0d0d0
        InactiveCommentDocKeyword = 0xffc0c0c0
        InactiveCommentDocKeywordError = 0xffc0c0c0
        InactiveCommentLine = 0xff90b090
        InactiveCommentLineDoc = 0xffc0c0c0
        InactiveDefault = 0xffc0c0c0
        InactiveDoubleQuotedString = 0xffb090b0
        InactiveGlobalClass = 0xffb0b0b0
        InactiveHashQuotedString = 0xffc3be98
        InactiveIdentifier = 0xffb0b0b0
        InactiveKeyword = 0xff9090b0
        InactiveKeywordSet2 = 0xffc0c0c0
        InactiveNumber = 0xff90b090
        InactiveOperator = 0xffb0b0b0
        InactivePreProcessor = 0xffb0b090
        InactivePreProcessorComment = 0xff1a0f0b
        InactivePreProcessorCommentLineDoc = 0xffc0c0c0
        InactiveRawString = 0xffc3be98
        InactiveRegex = 0xff7faf7f
        InactiveSingleQuotedString = 0xffb090b0
        InactiveTripleQuotedVerbatimString = 0xffc3be98
        InactiveUUID = 0xffc0c0c0
        InactiveUnclosedString = 0xffc3be98
        InactiveVerbatimString = 0xff90b090
        Keyword = 0xff519872
        KeywordSet2 = 0xffc3be98
        Number = 0xff6c9686
        Operator = 0xffc3be98
        PreProcessor = 0xff7f7f00
        PreProcessorComment = 0xff659900
        PreProcessorCommentLineDoc = 0xff3f703f
        RawString = 0xff7ca563
        Regex = 0xff3f7f3f
        SingleQuotedString = 0xff7ca563
        TripleQuotedVerbatimString = 0xff679d47
        UUID = 0xff804080
        UnclosedString = 0xffc3be98
        VerbatimString = 0xff679d47
    
    class Java:
        Comment = 0xff679d47
        CommentDoc = 0xff3f703f
        CommentDocKeyword = 0xff3060a0
        CommentDocKeywordError = 0xff804020
        CommentLine = 0xff679d47
        CommentLineDoc = 0xff3f703f
        Default = 0xff808080
        DoubleQuotedString = 0xff7ca563
        GlobalClass = 0xffc3be98
        HashQuotedString = 0xff679d47
        Identifier = 0xffc3be98
        InactiveComment = 0xff90b090
        InactiveCommentDoc = 0xffd0d0d0
        InactiveCommentDocKeyword = 0xffc0c0c0
        InactiveCommentDocKeywordError = 0xffc0c0c0
        InactiveCommentLine = 0xff90b090
        InactiveCommentLineDoc = 0xffc0c0c0
        InactiveDefault = 0xffc0c0c0
        InactiveDoubleQuotedString = 0xffb090b0
        InactiveGlobalClass = 0xffb0b0b0
        InactiveHashQuotedString = 0xffc3be98
        InactiveIdentifier = 0xffb0b0b0
        InactiveKeyword = 0xff9090b0
        InactiveKeywordSet2 = 0xffc0c0c0
        InactiveNumber = 0xff90b090
        InactiveOperator = 0xffb0b0b0
        InactivePreProcessor = 0xffb0b090
        InactivePreProcessorComment = 0xff1a0f0b
        InactivePreProcessorCommentLineDoc = 0xffc0c0c0
        InactiveRawString = 0xffc3be98
        InactiveRegex = 0xff7faf7f
        InactiveSingleQuotedString = 0xffb090b0
        InactiveTripleQuotedVerbatimString = 0xffc3be98
        InactiveUUID = 0xffc0c0c0
        InactiveUnclosedString = 0xffc3be98
        InactiveVerbatimString = 0xff90b090
        Keyword = 0xff519872
        KeywordSet2 = 0xffc3be98
        Number = 0xff6c9686
        Operator = 0xffc3be98
        PreProcessor = 0xff7f7f00
        PreProcessorComment = 0xff659900
        PreProcessorCommentLineDoc = 0xff3f703f
        RawString = 0xff7ca563
        Regex = 0xff3f7f3f
        SingleQuotedString = 0xff7ca563
        TripleQuotedVerbatimString = 0xff679d47
        UUID = 0xffc3be98
        UnclosedString = 0xffc3be98
        VerbatimString = 0xff679d47
    
    class JavaScript:
        Comment = 0xff679d47
        CommentDoc = 0xff3f703f
        CommentDocKeyword = 0xff3060a0
        CommentDocKeywordError = 0xff804020
        CommentLine = 0xff679d47
        CommentLineDoc = 0xff3f703f
        Default = 0xff808080
        DoubleQuotedString = 0xff7ca563
        GlobalClass = 0xffc3be98
        HashQuotedString = 0xff679d47
        Identifier = 0xffc3be98
        InactiveComment = 0xff90b090
        InactiveCommentDoc = 0xffd0d0d0
        InactiveCommentDocKeyword = 0xffc0c0c0
        InactiveCommentDocKeywordError = 0xffc0c0c0
        InactiveCommentLine = 0xff90b090
        InactiveCommentLineDoc = 0xffc0c0c0
        InactiveDefault = 0xffc0c0c0
        InactiveDoubleQuotedString = 0xffb090b0
        InactiveGlobalClass = 0xffb0b0b0
        InactiveHashQuotedString = 0xffc3be98
        InactiveIdentifier = 0xffb0b0b0
        InactiveKeyword = 0xff9090b0
        InactiveKeywordSet2 = 0xffc0c0c0
        InactiveNumber = 0xff90b090
        InactiveOperator = 0xffb0b0b0
        InactivePreProcessor = 0xffb0b090
        InactivePreProcessorComment = 0xff1a0f0b
        InactivePreProcessorCommentLineDoc = 0xffc0c0c0
        InactiveRawString = 0xffc3be98
        InactiveRegex = 0xff7faf7f
        InactiveSingleQuotedString = 0xffb090b0
        InactiveTripleQuotedVerbatimString = 0xffc3be98
        InactiveUUID = 0xffc0c0c0
        InactiveUnclosedString = 0xffc3be98
        InactiveVerbatimString = 0xff90b090
        Keyword = 0xff519872
        KeywordSet2 = 0xffc3be98
        Number = 0xff6c9686
        Operator = 0xffc3be98
        PreProcessor = 0xff7f7f00
        PreProcessorComment = 0xff659900
        PreProcessorCommentLineDoc = 0xff3f703f
        RawString = 0xff7ca563
        Regex = 0xff3f7f3f
        SingleQuotedString = 0xff7ca563
        TripleQuotedVerbatimString = 0xff679d47
        UUID = 0xffc3be98
        UnclosedString = 0xffc3be98
        VerbatimString = 0xff679d47
    
    class Lua:
        BasicFunctions = 0xff519872
        Character = 0xff7ca563
        Comment = 0xff679d47
        CoroutinesIOSystemFacilities = 0xff519872
        Default = 0xffc3be98
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        KeywordSet5 = 0xffc3be98
        KeywordSet6 = 0xffc3be98
        KeywordSet7 = 0xffc3be98
        KeywordSet8 = 0xffc3be98
        Label = 0xff7f7f00
        LineComment = 0xff679d47
        LiteralString = 0xff7ca563
        Number = 0xff6c9686
        Operator = 0xffc3be98
        Preprocessor = 0xff7f7f00
        String = 0xff7ca563
        StringTableMathsFunctions = 0xff519872
        UnclosedString = 0xffc3be98
    
    class Makefile:
        Comment = 0xff679d47
        Default = 0xffc3be98
        Error = 0xffffff00
        Operator = 0xffc3be98
        Preprocessor = 0xff7f7f00
        Target = 0xffa00000
        Variable = 0xff007fff
    
    class Matlab:
        Command = 0xff7f7f00
        Comment = 0xff679d47
        Default = 0xffc3be98
        DoubleQuotedString = 0xff7ca563
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        Number = 0xff6c9686
        Operator = 0xffc3be98
        SingleQuotedString = 0xff7ca563
    
    class Octave:
        Command = 0xff7f7f00
        Comment = 0xff679d47
        Default = 0xffc3be98
        DoubleQuotedString = 0xff7ca563
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        Number = 0xff6c9686
        Operator = 0xffc3be98
        SingleQuotedString = 0xff7ca563
    
    class PO:
        Comment = 0xff679d47
        Default = 0xffc3be98
        Flags = 0xffc3be98
        Fuzzy = 0xffc3be98
        MessageContext = 0xffc3be98
        MessageContextText = 0xffc3be98
        MessageContextTextEOL = 0xffc3be98
        MessageId = 0xffc3be98
        MessageIdText = 0xffc3be98
        MessageIdTextEOL = 0xffc3be98
        MessageString = 0xffc3be98
        MessageStringText = 0xffc3be98
        MessageStringTextEOL = 0xffc3be98
        ProgrammerComment = 0xff1a0f0b
        Reference = 0xffc3be98
    
    class POV:
        BadDirective = 0xff804020
        Comment = 0xff679d47
        CommentLine = 0xff679d47
        Default = 0xffff0080
        Directive = 0xff7f7f00
        Identifier = 0xffc3be98
        KeywordSet6 = 0xff519872
        KeywordSet7 = 0xff519872
        KeywordSet8 = 0xff519872
        Number = 0xff6c9686
        ObjectsCSGAppearance = 0xff519872
        Operator = 0xffc3be98
        PredefinedFunctions = 0xff519872
        PredefinedIdentifiers = 0xff519872
        String = 0xff7ca563
        TypesModifiersItems = 0xff519872
        UnclosedString = 0xffc3be98
    
    class Pascal:
        Asm = 0xff804080
        Character = 0xff7ca563
        Comment = 0xff679d47
        CommentLine = 0xff679d47
        CommentParenthesis = 0xff679d47
        Default = 0xff808080
        HexNumber = 0xff6c9686
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        Number = 0xff6c9686
        Operator = 0xffc3be98
        PreProcessor = 0xff7f7f00
        PreProcessorParenthesis = 0xff7f7f00
        SingleQuotedString = 0xff7ca563
        UnclosedString = 0xffc3be98
    
    class Perl:
        Array = 0xffc3be98
        BacktickHereDocument = 0xff7ca563
        BacktickHereDocumentVar = 0xffd00000
        Backticks = 0xffffff00
        BackticksVar = 0xffd00000
        Comment = 0xff679d47
        DataSection = 0xff600000
        Default = 0xff808080
        DoubleQuotedHereDocument = 0xff7ca563
        DoubleQuotedHereDocumentVar = 0xffd00000
        DoubleQuotedString = 0xff7ca563
        DoubleQuotedStringVar = 0xffd00000
        Error = 0xffffff00
        FormatBody = 0xffc000c0
        FormatIdentifier = 0xffc000c0
        Hash = 0xffc3be98
        HereDocumentDelimiter = 0xffc3be98
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        Number = 0xff6c9686
        Operator = 0xffc3be98
        POD = 0xff004000
        PODVerbatim = 0xff004000
        QuotedStringQ = 0xff7ca563
        QuotedStringQQ = 0xff7ca563
        QuotedStringQQVar = 0xffd00000
        QuotedStringQR = 0xffc3be98
        QuotedStringQRVar = 0xffd00000
        QuotedStringQW = 0xffc3be98
        QuotedStringQX = 0xffffff00
        QuotedStringQXVar = 0xffd00000
        Regex = 0xffc3be98
        RegexVar = 0xffd00000
        Scalar = 0xffc3be98
        SingleQuotedHereDocument = 0xff7ca563
        SingleQuotedString = 0xff7ca563
        SubroutinePrototype = 0xffc3be98
        Substitution = 0xffc3be98
        SubstitutionVar = 0xffd00000
        SymbolTable = 0xffc3be98
        Translation = 0xffc3be98
    
    class PostScript:
        ArrayParenthesis = 0xff519872
        BadStringCharacter = 0xffffff00
        Base85String = 0xff7ca563
        Comment = 0xff679d47
        DSCComment = 0xff3f703f
        DSCCommentValue = 0xff3060a0
        Default = 0xffc3be98
        DictionaryParenthesis = 0xff3060a0
        HexString = 0xff3f7f3f
        ImmediateEvalLiteral = 0xff7f7f00
        Keyword = 0xff519872
        Literal = 0xff7f7f00
        Name = 0xffc3be98
        Number = 0xff6c9686
        ProcedureParenthesis = 0xffc3be98
        Text = 0xff7ca563
    
    class Properties:
        Assignment = 0xffb06000
        Comment = 0xff6c9686
        Default = 0xffc3be98
        DefaultValue = 0xff7f7f00
        Key = 0xffc3be98
        Section = 0xff7ca563
    
    class Python:
        ClassName = 0xffb3935c
        Comment = 0xff679d47
        CommentBlock = 0xff7f7f7f
        Decorator = 0xff805000
        Default = 0xffc3be98
        DoubleQuotedString = 0xff7ca563
        FunctionMethodName = 0xff6c9686
        HighlightedIdentifier = 0xff407090
        Identifier = 0xffc3be98
        Inconsistent = 0xff679d47
        Keyword = 0xff519872
        NoWarning = 0xff808080
        Number = 0xff6c9686
        Operator = 0xffc3be98
        SingleQuotedString = 0xff7ca563
        Spaces = 0xff7ca563
        Tabs = 0xff7ca563
        TabsAfterSpaces = 0xff6c9686
        TripleDoubleQuotedString = 0xffe1aa7d
        TripleSingleQuotedString = 0xffe1aa7d
        UnclosedString = 0xffc3be98
    
    class Ruby:
        Backticks = 0xffffff00
        ClassName = 0xffb3935c
        ClassVariable = 0xff8000b0
        Comment = 0xff679d47
        DataSection = 0xff600000
        Default = 0xff808080
        DemotedKeyword = 0xff519872
        DoubleQuotedString = 0xff7ca563
        Error = 0xffc3be98
        FunctionMethodName = 0xff6c9686
        Global = 0xff800080
        HereDocument = 0xff7ca563
        HereDocumentDelimiter = 0xffc3be98
        Identifier = 0xffc3be98
        InstanceVariable = 0xffb00080
        Keyword = 0xff519872
        ModuleName = 0xffa000a0
        Number = 0xff6c9686
        Operator = 0xffc3be98
        POD = 0xff004000
        PercentStringQ = 0xff7ca563
        PercentStringq = 0xff7ca563
        PercentStringr = 0xffc3be98
        PercentStringw = 0xffc3be98
        PercentStringx = 0xffffff00
        Regex = 0xffc3be98
        SingleQuotedString = 0xff7ca563
        Stderr = 0xffc3be98
        Stdin = 0xffc3be98
        Stdout = 0xffc3be98
        Symbol = 0xffc0a030
    
    class SQL:
        Comment = 0xff679d47
        CommentDoc = 0xff7f7f7f
        CommentDocKeyword = 0xff3060a0
        CommentDocKeywordError = 0xff804020
        CommentLine = 0xff679d47
        CommentLineHash = 0xff679d47
        Default = 0xff808080
        DoubleQuotedString = 0xff7ca563
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        KeywordSet5 = 0xff4b0082
        KeywordSet6 = 0xffb00040
        KeywordSet7 = 0xff8b0000
        KeywordSet8 = 0xff800080
        Number = 0xff6c9686
        Operator = 0xffc3be98
        PlusComment = 0xff679d47
        PlusKeyword = 0xff7f7f00
        PlusPrompt = 0xff679d47
        QuotedIdentifier = 0xffc3be98
        SingleQuotedString = 0xff7ca563
    
    class Spice:
        Command = 0xff519872
        Comment = 0xff679d47
        Default = 0xff808080
        Delimiter = 0xffc3be98
        Function = 0xff519872
        Identifier = 0xffc3be98
        Number = 0xff6c9686
        Parameter = 0xff0040e0
        Value = 0xff7ca563
    
    class TCL:
        Comment = 0xff679d47
        CommentBlock = 0xffc3be98
        CommentBox = 0xff679d47
        CommentLine = 0xff679d47
        Default = 0xff808080
        ExpandKeyword = 0xff519872
        ITCLKeyword = 0xff519872
        Identifier = 0xff519872
        KeywordSet6 = 0xff519872
        KeywordSet7 = 0xff519872
        KeywordSet8 = 0xff519872
        KeywordSet9 = 0xff519872
        Modifier = 0xff7ca563
        Number = 0xff6c9686
        Operator = 0xffc3be98
        QuotedKeyword = 0xff7ca563
        QuotedString = 0xff7ca563
        Substitution = 0xff7f7f00
        SubstitutionBrace = 0xff7f7f00
        TCLKeyword = 0xff519872
        TkCommand = 0xff519872
        TkKeyword = 0xff519872
    
    class TeX:
        Command = 0xff679d47
        Default = 0xff3f3f3f
        Group = 0xffe1aa7d
        Special = 0xff6c9686
        Symbol = 0xff7f7f00
        Text = 0xffc3be98
    
    class VHDL:
        Attribute = 0xff804020
        Comment = 0xff679d47
        CommentLine = 0xff3f7f3f
        Default = 0xff800080
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        KeywordSet7 = 0xff804020
        Number = 0xff6c9686
        Operator = 0xffc3be98
        StandardFunction = 0xff808020
        StandardOperator = 0xff6c9686
        StandardPackage = 0xff208020
        StandardType = 0xff208080
        String = 0xff7ca563
        UnclosedString = 0xffc3be98
    
    class Verilog:
        Comment = 0xff679d47
        CommentBang = 0xff3f7f3f
        CommentLine = 0xff679d47
        Default = 0xff808080
        Identifier = 0xffc3be98
        Keyword = 0xff519872
        KeywordSet2 = 0xff6c9686
        Number = 0xff6c9686
        Operator = 0xff007070
        Preprocessor = 0xff7f7f00
        String = 0xff7ca563
        SystemTask = 0xff804020
        UnclosedString = 0xffc3be98
        UserKeywordSet = 0xff2a00ff
    
    class XML:
        ASPAtStart = 0xffc3be98
        ASPJavaScriptComment = 0xff679d47
        ASPJavaScriptCommentDoc = 0xff7f7f7f
        ASPJavaScriptCommentLine = 0xff679d47
        ASPJavaScriptDefault = 0xffc3be98
        ASPJavaScriptDoubleQuotedString = 0xff7ca563
        ASPJavaScriptKeyword = 0xff519872
        ASPJavaScriptNumber = 0xff6c9686
        ASPJavaScriptRegex = 0xffc3be98
        ASPJavaScriptSingleQuotedString = 0xff7ca563
        ASPJavaScriptStart = 0xff7f7f00
        ASPJavaScriptSymbol = 0xffc3be98
        ASPJavaScriptUnclosedString = 0xffc3be98
        ASPJavaScriptWord = 0xffc3be98
        ASPPythonClassName = 0xffb3935c
        ASPPythonComment = 0xff679d47
        ASPPythonDefault = 0xff808080
        ASPPythonDoubleQuotedString = 0xff7ca563
        ASPPythonFunctionMethodName = 0xff6c9686
        ASPPythonIdentifier = 0xffc3be98
        ASPPythonKeyword = 0xff519872
        ASPPythonNumber = 0xff6c9686
        ASPPythonOperator = 0xffc3be98
        ASPPythonSingleQuotedString = 0xff7ca563
        ASPPythonStart = 0xff808080
        ASPPythonTripleDoubleQuotedString = 0xffe1aa7d
        ASPPythonTripleSingleQuotedString = 0xffe1aa7d
        ASPStart = 0xffc3be98
        ASPVBScriptComment = 0xff008000
        ASPVBScriptDefault = 0xffc3be98
        ASPVBScriptIdentifier = 0xff007fff
        ASPVBScriptKeyword = 0xff007fff
        ASPVBScriptNumber = 0xff008080
        ASPVBScriptStart = 0xffc3be98
        ASPVBScriptString = 0xff800080
        ASPVBScriptUnclosedString = 0xff007fff
        ASPXCComment = 0xff1a0f0b
        Attribute = 0xff008080
        CDATA = 0xff800000
        Default = 0xffc3be98
        Entity = 0xff800080
        HTMLComment = 0xff808000
        HTMLDoubleQuotedString = 0xff7ca563
        HTMLNumber = 0xff6c9686
        HTMLSingleQuotedString = 0xff7ca563
        HTMLValue = 0xff608060
        JavaScriptComment = 0xff679d47
        JavaScriptCommentDoc = 0xff3f703f
        JavaScriptCommentLine = 0xff679d47
        JavaScriptDefault = 0xffc3be98
        JavaScriptDoubleQuotedString = 0xff7ca563
        JavaScriptKeyword = 0xff519872
        JavaScriptNumber = 0xff6c9686
        JavaScriptRegex = 0xffc3be98
        JavaScriptSingleQuotedString = 0xff7ca563
        JavaScriptStart = 0xff7f7f00
        JavaScriptSymbol = 0xffc3be98
        JavaScriptUnclosedString = 0xffc3be98
        JavaScriptWord = 0xffc3be98
        OtherInTag = 0xff800080
        PHPComment = 0xff999999
        PHPCommentLine = 0xff666666
        PHPDefault = 0xff000033
        PHPDoubleQuotedString = 0xff679d47
        PHPDoubleQuotedVariable = 0xff519872
        PHPKeyword = 0xff7ca563
        PHPNumber = 0xffcc9900
        PHPOperator = 0xffc3be98
        PHPSingleQuotedString = 0xff009f00
        PHPStart = 0xff800000
        PHPVariable = 0xff519872
        PythonClassName = 0xffb3935c
        PythonComment = 0xff679d47
        PythonDefault = 0xff808080
        PythonDoubleQuotedString = 0xff7ca563
        PythonFunctionMethodName = 0xff6c9686
        PythonIdentifier = 0xffc3be98
        PythonKeyword = 0xff519872
        PythonNumber = 0xff6c9686
        PythonOperator = 0xffc3be98
        PythonSingleQuotedString = 0xff7ca563
        PythonStart = 0xff808080
        PythonTripleDoubleQuotedString = 0xffe1aa7d
        PythonTripleSingleQuotedString = 0xffe1aa7d
        SGMLBlockDefault = 0xff000066
        SGMLCommand = 0xff007fff
        SGMLComment = 0xff808000
        SGMLDefault = 0xff007fff
        SGMLDoubleQuotedString = 0xff800000
        SGMLEntity = 0xff333333
        SGMLError = 0xff800000
        SGMLParameter = 0xff006600
        SGMLParameterComment = 0xff1a0f0b
        SGMLSingleQuotedString = 0xff993300
        SGMLSpecial = 0xff3366ff
        Script = 0xff007fff
        Tag = 0xff007fff
        UnknownAttribute = 0xff008080
        UnknownTag = 0xff007fff
        VBScriptComment = 0xff008000
        VBScriptDefault = 0xffc3be98
        VBScriptIdentifier = 0xff007fff
        VBScriptKeyword = 0xff007fff
        VBScriptNumber = 0xff008080
        VBScriptStart = 0xffc3be98
        VBScriptString = 0xff800080
        VBScriptUnclosedString = 0xff007fff
        XMLEnd = 0xff800080
        XMLStart = 0xff800080
        XMLTagEnd = 0xff007fff
    
    class YAML:
        Comment = 0xff008800
        Default = 0xffc3be98
        DocumentDelimiter= 0xff1a0f0b
        Identifier = 0xff000088
        Keyword = 0xff880088
        Number = 0xff880000
        Operator = 0xffc3be98
        Reference = 0xff008888
        SyntaxErrorMarker = 0xffffffff
        TextBlockMarker = 0xff333366


class Paper:
    Default = PyQt4.QtGui.QColor(0xff1a0f0b)
    
    class Ada:
        Default = 0xff1a0f0b
        Comment = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        String = 0xff1a0f0b
        Procedure = 0xff1a0f0b
        Number = 0xff1a0f0b
        Type = 0xff1a0f0b
        Package = 0xff1a0f0b
    
    class Nim:
        Default = 0xff1a0f0b
        Comment = 0xff1a0f0b
        BasicKeyword = 0xff1a0f0b
        TopKeyword = 0xff1a0f0b
        String = 0xff1a0f0b
        LongString = 0xff1a0f0b
        Number = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Unsafe = 0xff1a0f0b
        Type = 0xff1a0f0b
        DocumentationComment = 0xff1a0f0b
        Definition = 0xff1a0f0b
        Class = 0xff1a0f0b
        KeywordOperator = 0xff1a0f0b
        CharLiteral = 0xff1a0f0b
        CaseOf = 0xff1a0f0b
        UserKeyword = 0xff1a0f0b
        MultilineComment = 0xff1a0f0b
        MultilineDocumentation = 0xff1a0f0b
        Pragma = 0xff1a0f0b
    
    class Oberon:
        Default = 0xff1a0f0b
        Comment = 0xff1a0f0b
        Keyword = 0xff1a0f0b
        String = 0xff1a0f0b
        Procedure = 0xff1a0f0b
        Module = 0xff1a0f0b
        Number = 0xff1a0f0b
        Type = 0xff1a0f0b
    
    
    # Generated
    class AVS:
        Function= 0xff1a0f0b
        KeywordSet6= 0xff1a0f0b
        TripleString= 0xff1a0f0b
        LineComment = 0xff1a0f0b
        Plugin= 0xff1a0f0b
        String= 0xff1a0f0b
        ClipProperty= 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Number= 0xff1a0f0b
        Filter= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        NestedBlockComment = 0xff1a0f0b
        Keyword= 0xff1a0f0b
        BlockComment = 0xff1a0f0b
    
    class Bash:
        Error = 0xffff0000
        Backticks = 0xffa08080
        SingleQuotedHereDocument = 0xffddd0dd
        Scalar = 0xffffe0e0
        HereDocumentDelimiter = 0xffddd0dd
        Comment = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        ParameterExpansion = 0xffffffe0
        Number= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Keyword= 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
    
    class Batch:
        Label = 0xff606060
        Default = 0xff1a0f0b
        Keyword= 0xff1a0f0b
        ExternalCommand= 0xff1a0f0b
        Variable= 0xff1a0f0b
        Comment = 0xff1a0f0b
        HideCommandChar= 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class CMake:
        Function= 0xff1a0f0b
        BlockForeach= 0xff1a0f0b
        BlockWhile= 0xff1a0f0b
        StringLeftQuote = 0xffeeeeee
        Label= 0xff1a0f0b
        Comment = 0xff1a0f0b
        BlockMacro= 0xff1a0f0b
        StringRightQuote = 0xffeeeeee
        Default = 0xff1a0f0b
        Number= 0xff1a0f0b
        BlockIf= 0xff1a0f0b
        Variable= 0xff1a0f0b
        KeywordSet3= 0xff1a0f0b
        String = 0xffeeeeee
        StringVariable = 0xffeeeeee
    
    class CPP:
        CommentDocKeywordError= 0xff1a0f0b
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff1a0f0b
        UUID = 0xff1a0f0b
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        InactiveOperator = 0xff1a0f0b
        InactivePreProcessor = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff1a0f0b
        InactiveRawString = 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        KeywordSet2= 0xff1a0f0b
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine= 0xff1a0f0b
        InactiveNumber= 0xff1a0f0b
        InactivePreProcessorCommentLineDoc= 0xff1a0f0b
        Number= 0xff1a0f0b
        InactiveUUID = 0xff1a0f0b
        CommentDoc= 0xff1a0f0b
        InactiveCommentDoc= 0xff1a0f0b
        GlobalClass= 0xff1a0f0b
        InactiveSingleQuotedString = 0xff1a0f0b
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString= 0xff1a0f0b
        Regex = 0xffe0f0e0
        InactiveGlobalClass= 0xff1a0f0b
        InactiveIdentifier = 0xff1a0f0b
        CommentLineDoc= 0xff1a0f0b
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2= 0xff1a0f0b
        InactiveCommentDocKeyword= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        InactiveCommentLineDoc= 0xff1a0f0b
        InactiveDefault = 0xff1a0f0b
        InactiveCommentDocKeywordError= 0xff1a0f0b
        InactiveTripleQuotedVerbatimString= 0xff1a0f0b
        CommentDocKeyword= 0xff1a0f0b
        InactiveDoubleQuotedString= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        Comment = 0xff1a0f0b
        PreProcessorComment = 0xff1a0f0b
        InactiveComment = 0xff1a0f0b
        RawString = 0xfffff3ff
        Default = 0xff1a0f0b
        PreProcessorCommentLineDoc= 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        InactiveKeyword= 0xff1a0f0b
    
    class CSS:
        Important= 0xff1a0f0b
        CSS3Property= 0xff1a0f0b
        Attribute= 0xff1a0f0b
        Comment = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        MediaRule= 0xff1a0f0b
        AtRule= 0xff1a0f0b
        UnknownPseudoClass= 0xff1a0f0b
        PseudoClass= 0xff1a0f0b
        Tag= 0xff1a0f0b
        CSS2Property= 0xff1a0f0b
        CSS1Property= 0xff1a0f0b
        IDSelector= 0xff1a0f0b
        ExtendedCSSProperty= 0xff1a0f0b
        Variable= 0xff1a0f0b
        ExtendedPseudoClass= 0xff1a0f0b
        ClassSelector= 0xff1a0f0b
        Default = 0xff1a0f0b
        PseudoElement= 0xff1a0f0b
        UnknownProperty= 0xff1a0f0b
        Value= 0xff1a0f0b
        ExtendedPseudoElement= 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class CSharp:
        CommentDocKeywordError= 0xff1a0f0b
        InactiveRegex= 0xff1a0f0b
        InactivePreProcessorComment = 0xff1a0f0b
        UUID = 0xff1a0f0b
        InactiveVerbatimString= 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        InactiveOperator = 0xff1a0f0b
        InactivePreProcessor = 0xff1a0f0b
        UnclosedString= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        InactiveRawString = 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        KeywordSet2= 0xff1a0f0b
        InactiveUnclosedString= 0xff1a0f0b
        InactiveCommentLine= 0xff1a0f0b
        InactiveNumber= 0xff1a0f0b
        InactivePreProcessorCommentLineDoc= 0xff1a0f0b
        Number= 0xff1a0f0b
        InactiveUUID = 0xff1a0f0b
        CommentDoc= 0xff1a0f0b
        InactiveCommentDoc= 0xff1a0f0b
        GlobalClass= 0xff1a0f0b
        InactiveSingleQuotedString = 0xff1a0f0b
        HashQuotedString= 0xff1a0f0b
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString= 0xff1a0f0b
        Regex= 0xff1a0f0b
        InactiveGlobalClass= 0xff1a0f0b
        InactiveIdentifier = 0xff1a0f0b
        CommentLineDoc= 0xff1a0f0b
        TripleQuotedVerbatimString= 0xff1a0f0b
        InactiveKeywordSet2= 0xff1a0f0b
        InactiveCommentDocKeyword= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        InactiveCommentLineDoc= 0xff1a0f0b
        InactiveDefault = 0xff1a0f0b
        InactiveCommentDocKeywordError= 0xff1a0f0b
        InactiveTripleQuotedVerbatimString= 0xff1a0f0b
        CommentDocKeyword= 0xff1a0f0b
        InactiveDoubleQuotedString= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        Comment = 0xff1a0f0b
        PreProcessorComment = 0xff1a0f0b
        InactiveComment = 0xff1a0f0b
        RawString= 0xff1a0f0b
        Default = 0xff1a0f0b
        PreProcessorCommentLineDoc= 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        InactiveKeyword= 0xff1a0f0b
    
    class CoffeeScript:
        UUID = 0xff1a0f0b
        CommentDocKeywordError= 0xff1a0f0b
        GlobalClass= 0xff1a0f0b
        VerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Number= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Keyword= 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Regex = 0xffe0f0e0
        CommentDocKeyword= 0xff1a0f0b
        BlockRegex= 0xff1a0f0b
        CommentLineDoc= 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        CommentBlock= 0xff1a0f0b
        Comment = 0xff1a0f0b
        KeywordSet2= 0xff1a0f0b
        BlockRegexComment = 0xff1a0f0b
        Default = 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        CommentDoc= 0xff1a0f0b
    
    class D:
        BackquoteString= 0xff1a0f0b
        CommentDocKeywordError= 0xff1a0f0b
        Operator = 0xff1a0f0b
        CommentNested= 0xff1a0f0b
        KeywordDoc= 0xff1a0f0b
        KeywordSet7= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        KeywordSecondary= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        KeywordSet5= 0xff1a0f0b
        CommentDocKeyword= 0xff1a0f0b
        KeywordSet6= 0xff1a0f0b
        CommentLineDoc= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        Comment = 0xff1a0f0b
        Typedefs= 0xff1a0f0b
        Character= 0xff1a0f0b
        RawString= 0xff1a0f0b
        Default = 0xff1a0f0b
        Number= 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        String= 0xff1a0f0b
        CommentDoc= 0xff1a0f0b
    
    class Diff:
        Header= 0xff1a0f0b
        LineChanged= 0xff1a0f0b
        Default = 0xff1a0f0b
        LineRemoved= 0xff1a0f0b
        Command= 0xff1a0f0b
        Position= 0xff1a0f0b
        LineAdded= 0xff1a0f0b
        Comment = 0xff1a0f0b
    
    class Fortran:
        Label= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        DottedOperator = 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        Comment = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Default = 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        ExtendedFunction= 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Number= 0xff1a0f0b
        Continuation = 0xfff0e080
        IntrinsicFunction= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class Fortran77:
        Label= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        DottedOperator = 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        Comment = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Default = 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        ExtendedFunction= 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Number= 0xff1a0f0b
        Continuation = 0xfff0e080
        IntrinsicFunction= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class HTML:
        HTMLValue = 0xffffefff
        PythonDefault = 0xffefffef
        Entity= 0xff1a0f0b
        SGMLParameter = 0xffefefff
        SGMLDefault = 0xffefefff
        PHPVariable = 0xfffff8f8
        SGMLCommand = 0xffefefff
        PythonClassName = 0xffefffef
        VBScriptUnclosedString = 0xff7f7fff
        ASPJavaScriptDefault = 0xffdfdf7f
        ASPVBScriptStart= 0xff1a0f0b
        VBScriptDefault = 0xffefefff
        PythonNumber = 0xffefffef
        PythonOperator = 0xffefffef
        ASPJavaScriptSingleQuotedString = 0xffdfdf7f
        PHPDefault = 0xfffff8f8
        XMLStart= 0xff1a0f0b
        PythonFunctionMethodName = 0xffefffef
        ASPJavaScriptStart= 0xff1a0f0b
        JavaScriptWord = 0xfff0f0ff
        PHPSingleQuotedString = 0xfffff8f8
        PythonTripleDoubleQuotedString = 0xffefffef
        JavaScriptComment = 0xfff0f0ff
        Default = 0xff1a0f0b
        SGMLSingleQuotedString = 0xffefefff
        VBScriptComment = 0xffefefff
        ASPVBScriptNumber = 0xffcfcfef
        ASPJavaScriptCommentDoc = 0xffdfdf7f
        PythonIdentifier = 0xffefffef
        VBScriptKeyword = 0xffefefff
        JavaScriptDefault = 0xfff0f0ff
        PythonStart= 0xff1a0f0b
        ASPPythonComment = 0xffcfefcf
        ASPJavaScriptWord = 0xffdfdf7f
        SGMLParameterComment = 0xff1a0f0b
        JavaScriptSingleQuotedString = 0xfff0f0ff
        PythonSingleQuotedString = 0xffefffef
        HTMLSingleQuotedString = 0xff1a0f0b
        ASPVBScriptString = 0xffcfcfef
        SGMLBlockDefault = 0xffcccce0
        PythonKeyword = 0xffefffef
        XMLTagEnd= 0xff1a0f0b
        ASPVBScriptComment = 0xffcfcfef
        ASPPythonSingleQuotedString = 0xffcfefcf
        PHPDoubleQuotedVariable = 0xfffff8f8
        ASPJavaScriptComment = 0xffdfdf7f
        JavaScriptUnclosedString = 0xffbfbbb0
        JavaScriptDoubleQuotedString = 0xfff0f0ff
        UnknownAttribute= 0xff1a0f0b
        ASPPythonOperator = 0xffcfefcf
        ASPJavaScriptSymbol = 0xffdfdf7f
        ASPPythonFunctionMethodName = 0xffcfefcf
        SGMLDoubleQuotedString = 0xffefefff
        PHPOperator = 0xfffff8f8
        JavaScriptNumber = 0xfff0f0ff
        PythonDoubleQuotedString = 0xffefffef
        ASPAtStart = 0xffffff00
        Script= 0xff1a0f0b
        PHPCommentLine = 0xfffff8f8
        SGMLComment = 0xffefefff
        JavaScriptStart= 0xff1a0f0b
        ASPPythonIdentifier = 0xffcfefcf
        ASPVBScriptKeyword = 0xffcfcfef
        ASPPythonTripleDoubleQuotedString = 0xffcfefcf
        ASPPythonKeyword = 0xffcfefcf
        ASPJavaScriptNumber = 0xffdfdf7f
        PHPStart = 0xffffefbf
        PythonTripleSingleQuotedString = 0xffefffef
        PHPNumber = 0xfffff8f8
        ASPPythonDefault = 0xffcfefcf
        SGMLSpecial = 0xffefefff
        OtherInTag= 0xff1a0f0b
        JavaScriptCommentDoc = 0xfff0f0ff
        Tag= 0xff1a0f0b
        XMLEnd= 0xff1a0f0b
        CDATA = 0xffffdf00
        HTMLNumber= 0xff1a0f0b
        SGMLError = 0xffff6666
        PHPKeyword = 0xfffff8f8
        ASPVBScriptUnclosedString = 0xff7f7fff
        ASPPythonNumber = 0xffcfefcf
        VBScriptString = 0xffefefff
        ASPPythonClassName = 0xffcfefcf
        ASPPythonStart= 0xff1a0f0b
        JavaScriptRegex = 0xffffbbb0
        ASPJavaScriptUnclosedString = 0xffbfbbb0
        ASPJavaScriptCommentLine = 0xffdfdf7f
        SGMLEntity = 0xffefefff
        ASPJavaScriptDoubleQuotedString = 0xffdfdf7f
        ASPStart = 0xffffdf00
        Attribute= 0xff1a0f0b
        ASPJavaScriptKeyword = 0xffdfdf7f
        ASPVBScriptDefault = 0xffcfcfef
        ASPVBScriptIdentifier = 0xffcfcfef
        ASPJavaScriptRegex = 0xffffbbb0
        VBScriptNumber = 0xffefefff
        HTMLDoubleQuotedString= 0xff1a0f0b
        ASPXCComment = 0xff1a0f0b
        VBScriptStart= 0xff1a0f0b
        PHPDoubleQuotedString = 0xfffff8f8
        PHPComment = 0xfffff8f8
        ASPPythonTripleSingleQuotedString = 0xffcfefcf
        ASPPythonDoubleQuotedString = 0xffcfefcf
        JavaScriptKeyword = 0xfff0f0ff
        JavaScriptSymbol = 0xfff0f0ff
        VBScriptIdentifier = 0xffefefff
        HTMLComment = 0xff1a0f0b
        UnknownTag= 0xff1a0f0b
        JavaScriptCommentLine = 0xfff0f0ff
        PythonComment = 0xffefffef
    
    class IDL:
        CommentDocKeywordError= 0xff1a0f0b
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff1a0f0b
        UUID = 0xff1a0f0b
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        InactiveOperator = 0xff1a0f0b
        InactivePreProcessor = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff1a0f0b
        InactiveRawString = 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        KeywordSet2= 0xff1a0f0b
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine= 0xff1a0f0b
        InactiveNumber= 0xff1a0f0b
        InactivePreProcessorCommentLineDoc= 0xff1a0f0b
        Number= 0xff1a0f0b
        InactiveUUID = 0xff1a0f0b
        CommentDoc= 0xff1a0f0b
        InactiveCommentDoc= 0xff1a0f0b
        GlobalClass= 0xff1a0f0b
        InactiveSingleQuotedString = 0xff1a0f0b
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString= 0xff1a0f0b
        Regex = 0xffe0f0e0
        InactiveGlobalClass= 0xff1a0f0b
        InactiveIdentifier = 0xff1a0f0b
        CommentLineDoc= 0xff1a0f0b
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2= 0xff1a0f0b
        InactiveCommentDocKeyword= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        InactiveCommentLineDoc= 0xff1a0f0b
        InactiveDefault = 0xff1a0f0b
        InactiveCommentDocKeywordError= 0xff1a0f0b
        InactiveTripleQuotedVerbatimString= 0xff1a0f0b
        CommentDocKeyword= 0xff1a0f0b
        InactiveDoubleQuotedString= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        Comment = 0xff1a0f0b
        PreProcessorComment = 0xff1a0f0b
        InactiveComment = 0xff1a0f0b
        RawString = 0xfffff3ff
        Default = 0xff1a0f0b
        PreProcessorCommentLineDoc= 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        InactiveKeyword= 0xff1a0f0b
    
    class Java:
        CommentDocKeywordError= 0xff1a0f0b
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff1a0f0b
        UUID = 0xff1a0f0b
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        InactiveOperator = 0xff1a0f0b
        InactivePreProcessor = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff1a0f0b
        InactiveRawString = 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        KeywordSet2= 0xff1a0f0b
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine= 0xff1a0f0b
        InactiveNumber= 0xff1a0f0b
        InactivePreProcessorCommentLineDoc= 0xff1a0f0b
        Number= 0xff1a0f0b
        InactiveUUID = 0xff1a0f0b
        CommentDoc= 0xff1a0f0b
        InactiveCommentDoc= 0xff1a0f0b
        GlobalClass= 0xff1a0f0b
        InactiveSingleQuotedString = 0xff1a0f0b
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString= 0xff1a0f0b
        Regex = 0xffe0f0e0
        InactiveGlobalClass= 0xff1a0f0b
        InactiveIdentifier = 0xff1a0f0b
        CommentLineDoc= 0xff1a0f0b
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2= 0xff1a0f0b
        InactiveCommentDocKeyword= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        InactiveCommentLineDoc= 0xff1a0f0b
        InactiveDefault = 0xff1a0f0b
        InactiveCommentDocKeywordError= 0xff1a0f0b
        InactiveTripleQuotedVerbatimString= 0xff1a0f0b
        CommentDocKeyword= 0xff1a0f0b
        InactiveDoubleQuotedString= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        Comment = 0xff1a0f0b
        PreProcessorComment = 0xff1a0f0b
        InactiveComment = 0xff1a0f0b
        RawString = 0xfffff3ff
        Default = 0xff1a0f0b
        PreProcessorCommentLineDoc= 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        InactiveKeyword= 0xff1a0f0b
    
    class JavaScript:
        CommentDocKeywordError= 0xff1a0f0b
        InactiveRegex= 0xff1a0f0b
        InactivePreProcessorComment = 0xff1a0f0b
        UUID = 0xff1a0f0b
        InactiveVerbatimString= 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Operator = 0xff1a0f0b
        InactiveOperator = 0xff1a0f0b
        InactivePreProcessor = 0xff1a0f0b
        UnclosedString= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        InactiveRawString = 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        KeywordSet2= 0xff1a0f0b
        InactiveUnclosedString= 0xff1a0f0b
        InactiveCommentLine= 0xff1a0f0b
        InactiveNumber= 0xff1a0f0b
        InactivePreProcessorCommentLineDoc= 0xff1a0f0b
        Number= 0xff1a0f0b
        InactiveUUID = 0xff1a0f0b
        CommentDoc= 0xff1a0f0b
        InactiveCommentDoc= 0xff1a0f0b
        GlobalClass= 0xff1a0f0b
        InactiveSingleQuotedString = 0xff1a0f0b
        HashQuotedString= 0xff1a0f0b
        VerbatimString= 0xff1a0f0b
        InactiveHashQuotedString= 0xff1a0f0b
        Regex = 0xffe0f0ff
        InactiveGlobalClass= 0xff1a0f0b
        InactiveIdentifier = 0xff1a0f0b
        CommentLineDoc= 0xff1a0f0b
        TripleQuotedVerbatimString= 0xff1a0f0b
        InactiveKeywordSet2= 0xff1a0f0b
        InactiveCommentDocKeyword= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        InactiveCommentLineDoc= 0xff1a0f0b
        InactiveDefault = 0xff1a0f0b
        InactiveCommentDocKeywordError= 0xff1a0f0b
        InactiveTripleQuotedVerbatimString= 0xff1a0f0b
        CommentDocKeyword= 0xff1a0f0b
        InactiveDoubleQuotedString= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        Comment = 0xff1a0f0b
        PreProcessorComment = 0xff1a0f0b
        InactiveComment = 0xff1a0f0b
        RawString= 0xff1a0f0b
        Default = 0xff1a0f0b
        PreProcessorCommentLineDoc= 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        InactiveKeyword= 0xff1a0f0b
    
    class Lua:
        Label= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        StringTableMathsFunctions = 0xffd0d0ff
        CoroutinesIOSystemFacilities = 0xffffd0d0
        KeywordSet5= 0xff1a0f0b
        KeywordSet6= 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        LineComment = 0xff1a0f0b
        Comment = 0xffd0f0f0
        String= 0xff1a0f0b
        Character= 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        LiteralString = 0xffe0ffff
        Number= 0xff1a0f0b
        KeywordSet8= 0xff1a0f0b
        KeywordSet7= 0xff1a0f0b
        BasicFunctions = 0xffd0ffd0
        Keyword= 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
    
    class Makefile:
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Target= 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        Variable= 0xff1a0f0b
        Comment = 0xff1a0f0b
        Error = 0xffff0000
    
    class Matlab:
        SingleQuotedString = 0xff1a0f0b
        Default = 0xff1a0f0b
        Keyword= 0xff1a0f0b
        Number= 0xff1a0f0b
        Command= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Comment = 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class Octave:
        SingleQuotedString = 0xff1a0f0b
        Default = 0xff1a0f0b
        Keyword= 0xff1a0f0b
        Number= 0xff1a0f0b
        Command= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Comment = 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        Operator = 0xff1a0f0b
    
    class PO:
        ProgrammerComment = 0xff1a0f0b
        Flags= 0xff1a0f0b
        MessageContextText= 0xff1a0f0b
        MessageStringTextEOL= 0xff1a0f0b
        MessageId= 0xff1a0f0b
        MessageIdText= 0xff1a0f0b
        Reference= 0xff1a0f0b
        Comment = 0xff1a0f0b
        MessageStringText= 0xff1a0f0b
        MessageContext= 0xff1a0f0b
        Fuzzy= 0xff1a0f0b
        Default = 0xff1a0f0b
        MessageString= 0xff1a0f0b
        MessageContextTextEOL= 0xff1a0f0b
        MessageIdTextEOL= 0xff1a0f0b
    
    class POV:
        KeywordSet7 = 0xffd0d0d0
        KeywordSet6 = 0xffd0ffd0
        PredefinedFunctions = 0xffd0d0ff
        CommentLine= 0xff1a0f0b
        PredefinedIdentifiers= 0xff1a0f0b
        Comment = 0xff1a0f0b
        Directive= 0xff1a0f0b
        String= 0xff1a0f0b
        BadDirective= 0xff1a0f0b
        TypesModifiersItems = 0xffffffd0
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Number= 0xff1a0f0b
        KeywordSet8 = 0xffe0e0e0
        Identifier = 0xff1a0f0b
        ObjectsCSGAppearance = 0xffffd0d0
        UnclosedString = 0xffe0c0e0
    
    class Pascal:
        PreProcessorParenthesis= 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        Comment = 0xff1a0f0b
        CommentParenthesis= 0xff1a0f0b
        Asm= 0xff1a0f0b
        Character= 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Number= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Keyword= 0xff1a0f0b
        HexNumber= 0xff1a0f0b
    
    class Perl:
        Translation = 0xfff0e080
        BacktickHereDocument = 0xffddd0dd
        Array = 0xffffffe0
        QuotedStringQXVar = 0xffa08080
        PODVerbatim = 0xffc0ffc0
        DoubleQuotedStringVar= 0xff1a0f0b
        Regex = 0xffa0ffa0
        HereDocumentDelimiter = 0xffddd0dd
        SubroutinePrototype= 0xff1a0f0b
        BacktickHereDocumentVar = 0xffddd0dd
        QuotedStringQR= 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        QuotedStringQRVar= 0xff1a0f0b
        SubstitutionVar= 0xff1a0f0b
        Operator = 0xff1a0f0b
        DoubleQuotedHereDocumentVar = 0xffddd0dd
        Identifier = 0xff1a0f0b
        QuotedStringQX= 0xff1a0f0b
        BackticksVar = 0xffa08080
        Keyword= 0xff1a0f0b
        QuotedStringQ= 0xff1a0f0b
        QuotedStringQQVar= 0xff1a0f0b
        QuotedStringQQ= 0xff1a0f0b
        POD = 0xffe0ffe0
        FormatIdentifier = 0xff1a0f0b
        RegexVar= 0xff1a0f0b
        Backticks = 0xffa08080
        DoubleQuotedHereDocument = 0xffddd0dd
        Scalar = 0xffffe0e0
        FormatBody = 0xfffff0ff
        Comment = 0xff1a0f0b
        QuotedStringQW= 0xff1a0f0b
        SymbolTable = 0xffe0e0e0
        Default = 0xff1a0f0b
        Error = 0xffff0000
        SingleQuotedHereDocument = 0xffddd0dd
        Number= 0xff1a0f0b
        Hash = 0xffffe0ff
        Substitution = 0xfff0e080
        DataSection = 0xfffff0d8
        DoubleQuotedString= 0xff1a0f0b
    
    class PostScript:
        DictionaryParenthesis= 0xff1a0f0b
        HexString= 0xff1a0f0b
        DSCCommentValue= 0xff1a0f0b
        ProcedureParenthesis= 0xff1a0f0b
        Comment = 0xff1a0f0b
        ImmediateEvalLiteral= 0xff1a0f0b
        Name= 0xff1a0f0b
        DSCComment = 0xff1a0f0b
        Default = 0xff1a0f0b
        Base85String= 0xff1a0f0b
        Number= 0xff1a0f0b
        ArrayParenthesis= 0xff1a0f0b
        Literal= 0xff1a0f0b
        BadStringCharacter = 0xffff0000
        Text= 0xff1a0f0b
        Keyword= 0xff1a0f0b
    
    class Properties:
        DefaultValue= 0xff1a0f0b
        Default = 0xff1a0f0b
        Section = 0xffe0f0f0
        Assignment= 0xff1a0f0b
        Key= 0xff1a0f0b
        Comment = 0xff1a0f0b
    
    class Python:
        TripleDoubleQuotedString= 0xff1a0f0b
        FunctionMethodName= 0xff1a0f0b
        TabsAfterSpaces= 0xff1a0f0b
        Tabs= 0xff1a0f0b
        Decorator= 0xff1a0f0b
        NoWarning= 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
        Spaces= 0xff1a0f0b
        CommentBlock= 0xff1a0f0b
        Comment = 0xff1a0f0b
        TripleSingleQuotedString = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        Inconsistent= 0xff1a0f0b
        Default = 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        Operator = 0xff1a0f0b
        Number= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        ClassName= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        HighlightedIdentifier = 0xff1a0f0b
    
    class Ruby:
        Symbol= 0xff1a0f0b
        Stderr = 0xffff8080
        Global= 0xff1a0f0b
        FunctionMethodName= 0xff1a0f0b
        Stdin = 0xffff8080
        HereDocumentDelimiter = 0xffddd0dd
        PercentStringr = 0xffa0ffa0
        PercentStringQ= 0xff1a0f0b
        ModuleName= 0xff1a0f0b
        HereDocument = 0xffddd0dd
        SingleQuotedString = 0xff1a0f0b
        PercentStringQ= 0xff1a0f0b
        Regex = 0xffa0ffa0
        Operator = 0xff1a0f0b
        PercentStringw = 0xffffffe0
        PercentStringx = 0xffa08080
        POD = 0xffc0ffc0
        Keyword= 0xff1a0f0b
        Stdout = 0xffff8080
        ClassVariable= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        DemotedKeyword= 0xff1a0f0b
        Backticks = 0xffa08080
        InstanceVariable= 0xff1a0f0b
        Comment = 0xff1a0f0b
        Default = 0xff1a0f0b
        Error = 0xffff0000
        Number= 0xff1a0f0b
        DataSection = 0xfffff0d8
        ClassName= 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
    
    class SQL:
        PlusComment = 0xff1a0f0b
        KeywordSet7= 0xff1a0f0b
        PlusPrompt = 0xffe0ffe0
        CommentDocKeywordError= 0xff1a0f0b
        CommentDocKeyword= 0xff1a0f0b
        KeywordSet6= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        Comment = 0xff1a0f0b
        Operator = 0xff1a0f0b
        QuotedIdentifier = 0xff1a0f0b
        SingleQuotedString = 0xff1a0f0b
        PlusKeyword= 0xff1a0f0b
        Default = 0xff1a0f0b
        DoubleQuotedString= 0xff1a0f0b
        CommentLineHash= 0xff1a0f0b
        KeywordSet5= 0xff1a0f0b
        Number= 0xff1a0f0b
        KeywordSet8= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Keyword= 0xff1a0f0b
        CommentDoc= 0xff1a0f0b
    
    class Spice:
        Function= 0xff1a0f0b
        Delimiter= 0xff1a0f0b
        Value= 0xff1a0f0b
        Default = 0xff1a0f0b
        Number= 0xff1a0f0b
        Parameter= 0xff1a0f0b
        Command= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Comment = 0xff1a0f0b
    
    class TCL:
        SubstitutionBrace= 0xff1a0f0b
        CommentBox = 0xfff0fff0
        ITCLKeyword = 0xfffff0f0
        TkKeyword = 0xffe0fff0
        Operator = 0xff1a0f0b
        QuotedString = 0xfffff0f0
        ExpandKeyword = 0xffffff80
        KeywordSet7= 0xff1a0f0b
        TCLKeyword= 0xff1a0f0b
        TkCommand = 0xffffd0d0
        Identifier = 0xff1a0f0b
        KeywordSet6= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        CommentBlock = 0xfff0fff0
        Comment = 0xfff0ffe0
        Default = 0xff1a0f0b
        KeywordSet9= 0xff1a0f0b
        Modifier= 0xff1a0f0b
        Number= 0xff1a0f0b
        KeywordSet8= 0xff1a0f0b
        Substitution = 0xffeffff0
        QuotedKeyword = 0xfffff0f0
    
    class TeX:
        Symbol= 0xff1a0f0b
        Default = 0xff1a0f0b
        Command= 0xff1a0f0b
        Group= 0xff1a0f0b
        Text= 0xff1a0f0b
        Special= 0xff1a0f0b
    
    class VHDL:
        StandardOperator = 0xff1a0f0b
        Attribute= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        Comment = 0xff1a0f0b
        String= 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        StandardPackage= 0xff1a0f0b
        Number= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        KeywordSet7= 0xff1a0f0b
        StandardFunction= 0xff1a0f0b
        StandardType= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
    
    class Verilog:
        CommentBang = 0xffe0f0ff
        UserKeywordSet= 0xff1a0f0b
        PreProcessor= 0xff1a0f0b
        CommentLine= 0xff1a0f0b
        Comment = 0xff1a0f0b
        KeywordSet2= 0xff1a0f0b
        Default = 0xff1a0f0b
        Operator = 0xff1a0f0b
        Number= 0xff1a0f0b
        Identifier = 0xff1a0f0b
        SystemTask= 0xff1a0f0b
        String= 0xff1a0f0b
        Keyword= 0xff1a0f0b
        UnclosedString = 0xffe0c0e0
    
    class XML:
        HTMLValue = 0xffffefff
        PythonDefault = 0xffefffef
        Entity= 0xff1a0f0b
        SGMLParameter = 0xffefefff
        SGMLDefault = 0xffefefff
        PHPVariable = 0xfffff8f8
        SGMLCommand = 0xffefefff
        PythonClassName = 0xffefffef
        VBScriptUnclosedString = 0xff7f7fff
        ASPJavaScriptDefault = 0xffdfdf7f
        ASPVBScriptStart= 0xff1a0f0b
        VBScriptDefault = 0xffefefff
        PythonNumber = 0xffefffef
        PythonOperator = 0xffefffef
        ASPJavaScriptSingleQuotedString = 0xffdfdf7f
        PHPDefault = 0xfffff8f8
        XMLStart= 0xff1a0f0b
        PythonFunctionMethodName = 0xffefffef
        ASPJavaScriptStart= 0xff1a0f0b
        JavaScriptWord = 0xfff0f0ff
        PHPSingleQuotedString = 0xfffff8f8
        PythonTripleDoubleQuotedString = 0xffefffef
        JavaScriptComment = 0xfff0f0ff
        Default = 0xff1a0f0b
        SGMLSingleQuotedString = 0xffefefff
        VBScriptComment = 0xffefefff
        ASPVBScriptNumber = 0xffcfcfef
        ASPJavaScriptCommentDoc = 0xffdfdf7f
        PythonIdentifier = 0xffefffef
        VBScriptKeyword = 0xffefefff
        JavaScriptDefault = 0xfff0f0ff
        PythonStart= 0xff1a0f0b
        ASPPythonComment = 0xffcfefcf
        ASPJavaScriptWord = 0xffdfdf7f
        SGMLParameterComment = 0xff1a0f0b
        JavaScriptSingleQuotedString = 0xfff0f0ff
        PythonSingleQuotedString = 0xffefffef
        HTMLSingleQuotedString = 0xff1a0f0b
        ASPVBScriptString = 0xffcfcfef
        SGMLBlockDefault = 0xffcccce0
        PythonKeyword = 0xffefffef
        XMLTagEnd= 0xff1a0f0b
        ASPVBScriptComment = 0xffcfcfef
        ASPPythonSingleQuotedString = 0xffcfefcf
        PHPDoubleQuotedVariable = 0xfffff8f8
        ASPJavaScriptComment = 0xffdfdf7f
        JavaScriptUnclosedString = 0xffbfbbb0
        JavaScriptDoubleQuotedString = 0xfff0f0ff
        UnknownAttribute= 0xff1a0f0b
        ASPPythonOperator = 0xffcfefcf
        ASPJavaScriptSymbol = 0xffdfdf7f
        ASPPythonFunctionMethodName = 0xffcfefcf
        SGMLDoubleQuotedString = 0xffefefff
        PHPOperator = 0xfffff8f8
        JavaScriptNumber = 0xfff0f0ff
        PythonDoubleQuotedString = 0xffefffef
        ASPAtStart = 0xffffff00
        Script= 0xff1a0f0b
        PHPCommentLine = 0xfffff8f8
        SGMLComment = 0xffefefff
        JavaScriptStart= 0xff1a0f0b
        ASPPythonIdentifier = 0xffcfefcf
        ASPVBScriptKeyword = 0xffcfcfef
        ASPPythonTripleDoubleQuotedString = 0xffcfefcf
        ASPPythonKeyword = 0xffcfefcf
        ASPJavaScriptNumber = 0xffdfdf7f
        PHPStart = 0xffffefbf
        PythonTripleSingleQuotedString = 0xffefffef
        PHPNumber = 0xfffff8f8
        ASPPythonDefault = 0xffcfefcf
        SGMLSpecial = 0xffefefff
        OtherInTag= 0xff1a0f0b
        JavaScriptCommentDoc = 0xfff0f0ff
        Tag= 0xff1a0f0b
        XMLEnd= 0xff1a0f0b
        CDATA = 0xfffff0f0
        HTMLNumber= 0xff1a0f0b
        SGMLError = 0xffff6666
        PHPKeyword = 0xfffff8f8
        ASPVBScriptUnclosedString = 0xff7f7fff
        ASPPythonNumber = 0xffcfefcf
        VBScriptString = 0xffefefff
        ASPPythonClassName = 0xffcfefcf
        ASPPythonStart= 0xff1a0f0b
        JavaScriptRegex = 0xffffbbb0
        ASPJavaScriptUnclosedString = 0xffbfbbb0
        ASPJavaScriptCommentLine = 0xffdfdf7f
        SGMLEntity = 0xffefefff
        ASPJavaScriptDoubleQuotedString = 0xffdfdf7f
        ASPStart = 0xffffdf00
        Attribute= 0xff1a0f0b
        ASPJavaScriptKeyword = 0xffdfdf7f
        ASPVBScriptDefault = 0xffcfcfef
        ASPVBScriptIdentifier = 0xffcfcfef
        ASPJavaScriptRegex = 0xffffbbb0
        VBScriptNumber = 0xffefefff
        HTMLDoubleQuotedString= 0xff1a0f0b
        ASPXCComment = 0xff1a0f0b
        VBScriptStart= 0xff1a0f0b
        PHPDoubleQuotedString = 0xfffff8f8
        PHPComment = 0xfffff8f8
        ASPPythonTripleSingleQuotedString = 0xffcfefcf
        ASPPythonDoubleQuotedString = 0xffcfefcf
        JavaScriptKeyword = 0xfff0f0ff
        JavaScriptSymbol = 0xfff0f0ff
        VBScriptIdentifier = 0xffefefff
        HTMLComment = 0xff1a0f0b
        UnknownTag= 0xff1a0f0b
        JavaScriptCommentLine = 0xfff0f0ff
        PythonComment = 0xffefffef
    
    class YAML:
        TextBlockMarker= 0xff1a0f0b
        DocumentDelimiter = 0xff000088
        Operator = 0xff1a0f0b
        Number= 0xff1a0f0b
        Default = 0xff1a0f0b
        Identifier = 0xff1a0f0b
        Reference= 0xff1a0f0b
        Comment = 0xff1a0f0b
        Keyword= 0xff1a0f0b
        SyntaxErrorMarker = 0xffff0000
