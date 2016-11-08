
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
##      Water theme

import PyQt4.QtGui


Form = "#295a88"
Cursor = PyQt4.QtGui.QColor(0xffffffff)


class FoldMargin:
    ForeGround = PyQt4.QtGui.QColor(0xff4096bf)
    BackGround = PyQt4.QtGui.QColor(0xff3476a3)


class LineMargin:
    ForeGround = PyQt4.QtGui.QColor(0xffffffff)
    BackGround = PyQt4.QtGui.QColor(0xff1f4661)


class Indication:
    Font = "#e6e6e6"
    ActiveBackGround = "#112435"
    ActiveBorder = "#e6e6e6"
    PassiveBackGround = "#295a88"
    PassiveBorder = "#33aaff"


class TextDifferColors:
    Indicator_Unique_1_Color = PyQt4.QtGui.QColor(0x72, 0x9f, 0xcf, 80)
    Indicator_Unique_2_Color = PyQt4.QtGui.QColor(0xad, 0x7f, 0xa8, 80)
    Indicator_Similar_Color = PyQt4.QtGui.QColor(0x8a, 0xe2, 0x34, 80)

    
class Font:
    Default = PyQt4.QtGui.QColor(0xffffffff)
    
    class Repl:
        """
        THE MESSAGE COLORS ARE: 0xBBGGRR (BB-blue,GG-green,RR-red)
        """
        Error = 0x0000ff
        Warning = 0xe4761f
        Success = 0x007f00
        Diff_Unique_1 = 0xcf9f72
        Diff_Unique_2 = 0xa87fad
        Diff_Similar = 0x069a4e
    
    class Ada:
        Default = ('Courier', 0xffffffff, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        Procedure = ('Courier', 0xff5abcd8, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Type = ('Courier', 0xff2389da, 10, None)
        Package = ('Courier', 0xfff5b0cb, 10, None)
    
    class Nim:
        Default = ('Courier', 0xffffffff, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        BasicKeyword = ('Courier', 0xff2389da, 10, True)
        TopKeyword = ('Courier', 0xff407fc0, 10, True)
        String = ('Courier', 0xffc4bbb8, 10, None)
        LongString = ('Courier', 0xfff5b0cb, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xff7f7f7f, 10, None)
        Unsafe = ('Courier', 0xffc00000, 10, True)
        Type = ('Courier', 0xff6e6e00, 10, True)
        DocumentationComment = ('Courier', 0xffc75146, 10, None)
        Definition = ('Courier', 0xff74ccf4, 10, None)
        Class = ('Courier', 0xff5abcd8, 10, None)
        KeywordOperator = ('Courier', 0xff963cc8, 10, None)
        CharLiteral = ('Courier', 0xff00c8ff, 10, None)
        CaseOf = ('Courier', 0xff8000ff, 10, None)
        UserKeyword = ('Courier', 0xffff8040, 10, None)
        MultilineComment = ('Courier', 0xffad2e24, 10, None)
        MultilineDocumentation = ('Courier', 0xffea8c55, 10, None)
        Pragma = ('Courier', 0xffc07f40, 10, None)
    
    class Oberon:
        Default = ('Courier', 0xffffffff, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        Procedure = ('Courier', 0xff5abcd8, 10, None)
        Module = ('Courier', 0xfff5b0cb, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Type = ('Courier', 0xff2389da, 10, None)
    
    
    class AVS:
        BlockComment = ('Courier', 0xff6cab9d, 10, None)
        ClipProperty = ('Courier', 0xff2389da, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        Filter = ('Courier', 0xff2389da, 10, None)
        Function = ('Courier', 0xff74ccf4, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet6 = ('Courier', 0xff8000ff, 10, None)
        LineComment = ('Courier', 0xff6cab9d, 10, None)
        NestedBlockComment = ('Courier', 0xff6cab9d, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        Plugin = ('Courier', 0xff0080c0, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        TripleString = ('Courier', 0xffc4bbb8, 10, None)
    
    class Bash:
        Backticks = ('Courier', 0xffffff00, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc48e7b, 10, None)
        Error = ('Courier', 0xffffff00, 10, None)
        HereDocumentDelimiter = ('Courier', 0xffffffff, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        ParameterExpansion = ('Courier', 0xffffffff, 10, None)
        Scalar = ('Courier', 0xfffce94f, 10, True)
        SingleQuotedHereDocument = ('Courier', 0xffc4bbb8, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
    
    class Batch:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        ExternalCommand = ('Courier', 0xff2389da, 10, None)
        HideCommandChar = ('Courier', 0xff7f7f00, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        Label = ('Courier', 0xffc4bbb8, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        Variable = ('Courier', 0xff800080, 10, None)
    
    class CMake:
        BlockForeach = ('Courier', 0xff2389da, 10, None)
        BlockIf = ('Courier', 0xff2389da, 10, None)
        BlockMacro = ('Courier', 0xff2389da, 10, None)
        BlockWhile = ('Courier', 0xff2389da, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        Function = ('Courier', 0xff2389da, 10, None)
        KeywordSet3 = ('Courier', 0xffffffff, 10, None)
        Label = ('Courier', 0xffcc3300, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        StringLeftQuote = ('Courier', 0xffc4bbb8, 10, None)
        StringRightQuote = ('Courier', 0xffc4bbb8, 10, None)
        StringVariable = ('Courier', 0xffcc3300, 10, None)
        Variable = ('Courier', 0xffedff86, 10, None)
    
    class CPP:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffffffff, 10, None)
        HashQuotedString = ('Courier', 0xff6cab9d, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xffffffff, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xffffffff, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xffffffff, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xffffffff, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xffffffff, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet2 = ('Courier', 0xffffffff, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xffc4bbb8, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff6cab9d, 10, None)
        UUID = ('Courier', 0xffffffff, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class CSS:
        AtRule = ('Courier', 0xff7f7f00, 10, None)
        Attribute = ('Courier', 0xffedff86, 10, None)
        CSS1Property = ('Courier', 0xff0040e0, 10, None)
        CSS2Property = ('Courier', 0xff00a0e0, 10, None)
        CSS3Property = ('Courier', 0xffffffff, 10, None)
        ClassSelector = ('Courier', 0xffffffff, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffff0080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ExtendedCSSProperty = ('Courier', 0xffffffff, 10, None)
        ExtendedPseudoClass = ('Courier', 0xffffffff, 10, None)
        ExtendedPseudoElement = ('Courier', 0xffffffff, 10, None)
        IDSelector = ('Courier', 0xff74ccf4, 10, None)
        Important = ('Courier', 0xffff8000, 10, None)
        MediaRule = ('Courier', 0xff7f7f00, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PseudoClass = ('Courier', 0xffedff86, 10, None)
        PseudoElement = ('Courier', 0xffffffff, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Tag = ('Courier', 0xff2389da, 10, None)
        UnknownProperty = ('Courier', 0xffff0000, 10, None)
        UnknownPseudoClass = ('Courier', 0xffff0000, 10, None)
        Value = ('Courier', 0xffc4bbb8, 10, None)
        Variable = ('Courier', 0xffffffff, 10, None)
    
    class CSharp:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffffffff, 10, None)
        HashQuotedString = ('Courier', 0xff6cab9d, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xffffffff, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xffffffff, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xffffffff, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xffffffff, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xffffffff, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet2 = ('Courier', 0xffffffff, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xffc4bbb8, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff6cab9d, 10, None)
        UUID = ('Courier', 0xffffffff, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class CoffeeScript:
        BlockRegex = ('Courier', 0xff3f7f3f, 10, None)
        BlockRegexComment = ('Courier', 0xff6cab9d, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentBlock = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffffffff, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet2 = ('Courier', 0xffffffff, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        UUID = ('Courier', 0xffffffff, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class D:
        BackquoteString = ('Courier', 0xffffffff, 10, None)
        Character = ('Courier', 0xffc4bbb8, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        CommentNested = ('Courier', 0xffa0c0a0, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordDoc = ('Courier', 0xff2389da, 10, None)
        KeywordSecondary = ('Courier', 0xff2389da, 10, None)
        KeywordSet5 = ('Courier', 0xffffffff, 10, None)
        KeywordSet6 = ('Courier', 0xffffffff, 10, None)
        KeywordSet7 = ('Courier', 0xffffffff, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        RawString = ('Courier', 0xffffffff, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        Typedefs = ('Courier', 0xff2389da, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
    
    class Diff:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        Header = ('Courier', 0xfff5b0cb, 10, None)
        LineAdded = ('Courier', 0xff2389da, 10, None)
        LineChanged = ('Courier', 0xff7f7f7f, 10, None)
        LineRemoved = ('Courier', 0xff74ccf4, 10, None)
        Position = ('Courier', 0xffc4bbb8, 10, None)
    
    class Fortran:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Continuation = ('Courier', 0xffffffff, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DottedOperator = ('Courier', 0xffffffff, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ExtendedFunction = ('Courier', 0xffb04080, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        IntrinsicFunction = ('Courier', 0xffb00040, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        Label = ('Courier', 0xffe0c0e0, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
    
    class Fortran77:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Continuation = ('Courier', 0xffffffff, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DottedOperator = ('Courier', 0xffffffff, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ExtendedFunction = ('Courier', 0xffb04080, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        IntrinsicFunction = ('Courier', 0xffb00040, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        Label = ('Courier', 0xffe0c0e0, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
    
    class HTML:
        ASPAtStart = ('Courier', 0xffffffff, 10, None)
        ASPJavaScriptComment = ('Courier', 0xff6cab9d, 10, None)
        ASPJavaScriptCommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        ASPJavaScriptCommentLine = ('Courier', 0xff6cab9d, 10, None)
        ASPJavaScriptDefault = ('Courier', 0xffffffff, 10, None)
        ASPJavaScriptDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPJavaScriptKeyword = ('Courier', 0xff2389da, 10, None)
        ASPJavaScriptNumber = ('Courier', 0xff74ccf4, 10, None)
        ASPJavaScriptRegex = ('Courier', 0xffffffff, 10, None)
        ASPJavaScriptSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPJavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        ASPJavaScriptSymbol = ('Courier', 0xffffffff, 10, None)
        ASPJavaScriptUnclosedString = ('Courier', 0xffffffff, 10, None)
        ASPJavaScriptWord = ('Courier', 0xffffffff, 10, None)
        ASPPythonClassName = ('Courier', 0xff5abcd8, 10, None)
        ASPPythonComment = ('Courier', 0xff6cab9d, 10, None)
        ASPPythonDefault = ('Courier', 0xff808080, 10, None)
        ASPPythonDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPPythonFunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        ASPPythonIdentifier = ('Courier', 0xffffffff, 10, None)
        ASPPythonKeyword = ('Courier', 0xff2389da, 10, None)
        ASPPythonNumber = ('Courier', 0xff74ccf4, 10, None)
        ASPPythonOperator = ('Courier', 0xffffffff, 10, None)
        ASPPythonSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPPythonStart = ('Courier', 0xff808080, 10, None)
        ASPPythonTripleDoubleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        ASPPythonTripleSingleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        ASPStart = ('Courier', 0xffffffff, 10, None)
        ASPVBScriptComment = ('Courier', 0xff008000, 10, None)
        ASPVBScriptDefault = ('Courier', 0xffffffff, 10, None)
        ASPVBScriptIdentifier = ('Courier', 0xff1f76e4, 10, None)
        ASPVBScriptKeyword = ('Courier', 0xff1f76e4, 10, None)
        ASPVBScriptNumber = ('Courier', 0xff008080, 10, None)
        ASPVBScriptStart = ('Courier', 0xffffffff, 10, None)
        ASPVBScriptString = ('Courier', 0xff800080, 10, None)
        ASPVBScriptUnclosedString = ('Courier', 0xff1f76e4, 10, None)
        ASPXCComment = ('Courier', 0xffffffff, 10, None)
        Attribute = ('Courier', 0xff008080, 10, None)
        CDATA = ('Courier', 0xffffffff, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        Entity = ('Courier', 0xff800080, 10, None)
        HTMLComment = ('Courier', 0xff808000, 10, None)
        HTMLDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        HTMLNumber = ('Courier', 0xff74ccf4, 10, None)
        HTMLSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        HTMLValue = ('Courier', 0xffff00ff, 10, None)
        JavaScriptComment = ('Courier', 0xff6cab9d, 10, None)
        JavaScriptCommentDoc = ('Courier', 0xff3f703f, 10, None)
        JavaScriptCommentLine = ('Courier', 0xff6cab9d, 10, None)
        JavaScriptDefault = ('Courier', 0xffffffff, 10, None)
        JavaScriptDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        JavaScriptKeyword = ('Courier', 0xff2389da, 10, None)
        JavaScriptNumber = ('Courier', 0xff74ccf4, 10, None)
        JavaScriptRegex = ('Courier', 0xffffffff, 10, None)
        JavaScriptSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        JavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        JavaScriptSymbol = ('Courier', 0xffffffff, 10, None)
        JavaScriptUnclosedString = ('Courier', 0xffffffff, 10, None)
        JavaScriptWord = ('Courier', 0xffffffff, 10, None)
        OtherInTag = ('Courier', 0xff800080, 10, None)
        PHPComment = ('Courier', 0xff999999, 10, None)
        PHPCommentLine = ('Courier', 0xff666666, 10, None)
        PHPDefault = ('Courier', 0xffc7dbf5, 10, None)
        PHPDoubleQuotedString = ('Courier', 0xff6cab9d, 10, None)
        PHPDoubleQuotedVariable = ('Courier', 0xff2389da, 10, None)
        PHPKeyword = ('Courier', 0xffc4bbb8, 10, None)
        PHPNumber = ('Courier', 0xffcc9900, 10, None)
        PHPOperator = ('Courier', 0xffffffff, 10, None)
        PHPSingleQuotedString = ('Courier', 0xff009f00, 10, None)
        PHPStart = ('Courier', 0xff5abcd8, 10, None)
        PHPVariable = ('Courier', 0xff2389da, 10, None)
        PythonClassName = ('Courier', 0xff5abcd8, 10, None)
        PythonComment = ('Courier', 0xff6cab9d, 10, None)
        PythonDefault = ('Courier', 0xff808080, 10, None)
        PythonDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        PythonFunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        PythonIdentifier = ('Courier', 0xffffffff, 10, None)
        PythonKeyword = ('Courier', 0xff2389da, 10, None)
        PythonNumber = ('Courier', 0xff74ccf4, 10, None)
        PythonOperator = ('Courier', 0xffffffff, 10, None)
        PythonSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        PythonStart = ('Courier', 0xff808080, 10, None)
        PythonTripleDoubleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        PythonTripleSingleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        SGMLBlockDefault = ('Courier', 0xfffff5b2, 10, None)
        SGMLCommand = ('Courier', 0xff1f76e4, 10, None)
        SGMLComment = ('Courier', 0xff808000, 10, None)
        SGMLDefault = ('Courier', 0xff1f76e4, 10, None)
        SGMLDoubleQuotedString = ('Courier', 0xffedff86, 10, None)
        SGMLEntity = ('Courier', 0xff333333, 10, None)
        SGMLError = ('Courier', 0xffedff86, 10, None)
        SGMLParameter = ('Courier', 0xff006600, 10, None)
        SGMLParameterComment = ('Courier', 0xffffffff, 10, None)
        SGMLSingleQuotedString = ('Courier', 0xff993300, 10, None)
        SGMLSpecial = ('Courier', 0xff3366ff, 10, None)
        Script = ('Courier', 0xff1f76e4, 10, None)
        Tag = ('Courier', 0xff1f76e4, 10, None)
        UnknownAttribute = ('Courier', 0xffff0000, 10, None)
        UnknownTag = ('Courier', 0xffff0000, 10, None)
        VBScriptComment = ('Courier', 0xff008000, 10, None)
        VBScriptDefault = ('Courier', 0xffffffff, 10, None)
        VBScriptIdentifier = ('Courier', 0xff1f76e4, 10, None)
        VBScriptKeyword = ('Courier', 0xff1f76e4, 10, None)
        VBScriptNumber = ('Courier', 0xff008080, 10, None)
        VBScriptStart = ('Courier', 0xffffffff, 10, None)
        VBScriptString = ('Courier', 0xff800080, 10, None)
        VBScriptUnclosedString = ('Courier', 0xff1f76e4, 10, None)
        XMLEnd = ('Courier', 0xff5abcd8, 10, None)
        XMLStart = ('Courier', 0xff5abcd8, 10, None)
        XMLTagEnd = ('Courier', 0xff1f76e4, 10, None)
    
    class IDL:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffffffff, 10, None)
        HashQuotedString = ('Courier', 0xff6cab9d, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xffffffff, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xffffffff, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xffffffff, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xffffffff, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xffffffff, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet2 = ('Courier', 0xffffffff, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xffc4bbb8, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff6cab9d, 10, None)
        UUID = ('Courier', 0xff804080, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class Java:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffffffff, 10, None)
        HashQuotedString = ('Courier', 0xff6cab9d, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xffffffff, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xffffffff, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xffffffff, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xffffffff, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xffffffff, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet2 = ('Courier', 0xffffffff, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xffc4bbb8, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff6cab9d, 10, None)
        UUID = ('Courier', 0xffffffff, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class JavaScript:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffffffff, 10, None)
        HashQuotedString = ('Courier', 0xff6cab9d, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xffffffff, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xffffffff, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xffffffff, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xffffffff, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xffffffff, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet2 = ('Courier', 0xffffffff, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xffc4bbb8, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff6cab9d, 10, None)
        UUID = ('Courier', 0xffffffff, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class Lua:
        BasicFunctions = ('Courier', 0xff2389da, 10, None)
        Character = ('Courier', 0xffc4bbb8, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CoroutinesIOSystemFacilities = ('Courier', 0xff2389da, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet5 = ('Courier', 0xffffffff, 10, None)
        KeywordSet6 = ('Courier', 0xffffffff, 10, None)
        KeywordSet7 = ('Courier', 0xffffffff, 10, None)
        KeywordSet8 = ('Courier', 0xffffffff, 10, None)
        Label = ('Courier', 0xff7f7f00, 10, None)
        LineComment = ('Courier', 0xff6cab9d, 10, None)
        LiteralString = ('Courier', 0xffc4bbb8, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        StringTableMathsFunctions = ('Courier', 0xff2389da, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
    
    class Makefile:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        Error = ('Courier', 0xffffff00, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        Target = ('Courier', 0xffa00000, 10, None)
        Variable = ('Courier', 0xff1f76e4, 10, None)
    
    class Matlab:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
    
    class Octave:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
    
    class PO:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        Flags = ('Courier', 0xffffffff, 10, None)
        Fuzzy = ('Courier', 0xffffffff, 10, None)
        MessageContext = ('Courier', 0xffffffff, 10, None)
        MessageContextText = ('Courier', 0xffffffff, 10, None)
        MessageContextTextEOL = ('Courier', 0xffffffff, 10, None)
        MessageId = ('Courier', 0xffffffff, 10, None)
        MessageIdText = ('Courier', 0xffffffff, 10, None)
        MessageIdTextEOL = ('Courier', 0xffffffff, 10, None)
        MessageString = ('Courier', 0xffffffff, 10, None)
        MessageStringText = ('Courier', 0xffffffff, 10, None)
        MessageStringTextEOL = ('Courier', 0xffffffff, 10, None)
        ProgrammerComment = ('Courier', 0xffffffff, 10, None)
        Reference = ('Courier', 0xffffffff, 10, None)
    
    class POV:
        BadDirective = ('Courier', 0xff804020, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffff0080, 10, None)
        Directive = ('Courier', 0xff7f7f00, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        KeywordSet6 = ('Courier', 0xff2389da, 10, None)
        KeywordSet7 = ('Courier', 0xff2389da, 10, None)
        KeywordSet8 = ('Courier', 0xff2389da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        ObjectsCSGAppearance = ('Courier', 0xff2389da, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PredefinedFunctions = ('Courier', 0xff2389da, 10, None)
        PredefinedIdentifiers = ('Courier', 0xff2389da, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        TypesModifiersItems = ('Courier', 0xff2389da, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
    
    class Pascal:
        Asm = ('Courier', 0xff804080, 10, None)
        Character = ('Courier', 0xffc4bbb8, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentParenthesis = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        HexNumber = ('Courier', 0xff74ccf4, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorParenthesis = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
    
    class Perl:
        Array = ('Courier', 0xffffffff, 10, None)
        BacktickHereDocument = ('Courier', 0xffc4bbb8, 10, None)
        BacktickHereDocumentVar = ('Courier', 0xffd00000, 10, None)
        Backticks = ('Courier', 0xffffff00, 10, None)
        BackticksVar = ('Courier', 0xffd00000, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        DataSection = ('Courier', 0xff600000, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedHereDocument = ('Courier', 0xffc4bbb8, 10, None)
        DoubleQuotedHereDocumentVar = ('Courier', 0xffd00000, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        DoubleQuotedStringVar = ('Courier', 0xffd00000, 10, None)
        Error = ('Courier', 0xffffff00, 10, None)
        FormatBody = ('Courier', 0xffc000c0, 10, None)
        FormatIdentifier = ('Courier', 0xffc000c0, 10, None)
        Hash = ('Courier', 0xffffffff, 10, None)
        HereDocumentDelimiter = ('Courier', 0xffffffff, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        POD = ('Courier', 0xff004000, 10, None)
        PODVerbatim = ('Courier', 0xff004000, 10, None)
        QuotedStringQ = ('Courier', 0xffc4bbb8, 10, None)
        QuotedStringQQ = ('Courier', 0xffc4bbb8, 10, None)
        QuotedStringQQVar = ('Courier', 0xffd00000, 10, None)
        QuotedStringQR = ('Courier', 0xffffffff, 10, None)
        QuotedStringQRVar = ('Courier', 0xffd00000, 10, None)
        QuotedStringQW = ('Courier', 0xffffffff, 10, None)
        QuotedStringQX = ('Courier', 0xffffff00, 10, None)
        QuotedStringQXVar = ('Courier', 0xffd00000, 10, None)
        Regex = ('Courier', 0xffffffff, 10, None)
        RegexVar = ('Courier', 0xffd00000, 10, None)
        Scalar = ('Courier', 0xffffffff, 10, None)
        SingleQuotedHereDocument = ('Courier', 0xffc4bbb8, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        SubroutinePrototype = ('Courier', 0xffffffff, 10, None)
        Substitution = ('Courier', 0xffffffff, 10, None)
        SubstitutionVar = ('Courier', 0xffd00000, 10, None)
        SymbolTable = ('Courier', 0xffffffff, 10, None)
        Translation = ('Courier', 0xffffffff, 10, None)
    
    class PostScript:
        ArrayParenthesis = ('Courier', 0xff2389da, 10, None)
        BadStringCharacter = ('Courier', 0xffffff00, 10, None)
        Base85String = ('Courier', 0xffc4bbb8, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        DSCComment = ('Courier', 0xff3f703f, 10, None)
        DSCCommentValue = ('Courier', 0xff3060a0, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        DictionaryParenthesis = ('Courier', 0xff3060a0, 10, None)
        HexString = ('Courier', 0xff3f7f3f, 10, None)
        ImmediateEvalLiteral = ('Courier', 0xff7f7f00, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        Literal = ('Courier', 0xff7f7f00, 10, None)
        Name = ('Courier', 0xffffffff, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        ProcedureParenthesis = ('Courier', 0xffffffff, 10, None)
        Text = ('Courier', 0xffc4bbb8, 10, None)
    
    class Properties:
        Assignment = ('Courier', 0xffb06000, 10, None)
        Comment = ('Courier', 0xff74ccf4, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        DefaultValue = ('Courier', 0xff7f7f00, 10, None)
        Key = ('Courier', 0xffffffff, 10, None)
        Section = ('Courier', 0xffc4bbb8, 10, None)
    
    class Python:
        ClassName = ('Courier', 0xff5abcd8, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentBlock = ('Courier', 0xff7f7f7f, 10, None)
        Decorator = ('Courier', 0xff805000, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        FunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        HighlightedIdentifier = ('Courier', 0xff407090, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Inconsistent = ('Courier', 0xff6cab9d, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        NoWarning = ('Courier', 0xff808080, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Spaces = ('Courier', 0xffc4bbb8, 10, None)
        Tabs = ('Courier', 0xffc4bbb8, 10, None)
        TabsAfterSpaces = ('Courier', 0xff74ccf4, 10, None)
        TripleDoubleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        TripleSingleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
    
    class Ruby:
        Backticks = ('Courier', 0xffffff00, 10, None)
        ClassName = ('Courier', 0xff5abcd8, 10, None)
        ClassVariable = ('Courier', 0xff8000b0, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        DataSection = ('Courier', 0xff600000, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DemotedKeyword = ('Courier', 0xff2389da, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Error = ('Courier', 0xffffffff, 10, None)
        FunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        Global = ('Courier', 0xff800080, 10, None)
        HereDocument = ('Courier', 0xffc4bbb8, 10, None)
        HereDocumentDelimiter = ('Courier', 0xffffffff, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        InstanceVariable = ('Courier', 0xffb00080, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        ModuleName = ('Courier', 0xffa000a0, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        POD = ('Courier', 0xff004000, 10, None)
        PercentStringQ = ('Courier', 0xffc4bbb8, 10, None)
        PercentStringq = ('Courier', 0xffc4bbb8, 10, None)
        PercentStringr = ('Courier', 0xffffffff, 10, None)
        PercentStringw = ('Courier', 0xffffffff, 10, None)
        PercentStringx = ('Courier', 0xffffff00, 10, None)
        Regex = ('Courier', 0xffffffff, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Stderr = ('Courier', 0xffffffff, 10, None)
        Stdin = ('Courier', 0xffffffff, 10, None)
        Stdout = ('Courier', 0xffffffff, 10, None)
        Symbol = ('Courier', 0xffc0a030, 10, None)
    
    class SQL:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineHash = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet5 = ('Courier', 0xff4b0082, 10, None)
        KeywordSet6 = ('Courier', 0xffb00040, 10, None)
        KeywordSet7 = ('Courier', 0xff8b0000, 10, None)
        KeywordSet8 = ('Courier', 0xff800080, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        PlusComment = ('Courier', 0xff6cab9d, 10, None)
        PlusKeyword = ('Courier', 0xff7f7f00, 10, None)
        PlusPrompt = ('Courier', 0xff6cab9d, 10, None)
        QuotedIdentifier = ('Courier', 0xffffffff, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
    
    class Spice:
        Command = ('Courier', 0xff2389da, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Delimiter = ('Courier', 0xffffffff, 10, None)
        Function = ('Courier', 0xff2389da, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Parameter = ('Courier', 0xff0040e0, 10, None)
        Value = ('Courier', 0xffc4bbb8, 10, None)
    
    class TCL:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentBlock = ('Courier', 0xffffffff, 10, None)
        CommentBox = ('Courier', 0xff6cab9d, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        ExpandKeyword = ('Courier', 0xff2389da, 10, None)
        ITCLKeyword = ('Courier', 0xff2389da, 10, None)
        Identifier = ('Courier', 0xff2389da, 10, None)
        KeywordSet6 = ('Courier', 0xff2389da, 10, None)
        KeywordSet7 = ('Courier', 0xff2389da, 10, None)
        KeywordSet8 = ('Courier', 0xff2389da, 10, None)
        KeywordSet9 = ('Courier', 0xff2389da, 10, None)
        Modifier = ('Courier', 0xffc4bbb8, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        QuotedKeyword = ('Courier', 0xffc4bbb8, 10, None)
        QuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Substitution = ('Courier', 0xff7f7f00, 10, None)
        SubstitutionBrace = ('Courier', 0xff7f7f00, 10, None)
        TCLKeyword = ('Courier', 0xff2389da, 10, None)
        TkCommand = ('Courier', 0xff2389da, 10, None)
        TkKeyword = ('Courier', 0xff2389da, 10, None)
    
    class TeX:
        Command = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff3f3f3f, 10, None)
        Group = ('Courier', 0xfff5b0cb, 10, None)
        Special = ('Courier', 0xff74ccf4, 10, None)
        Symbol = ('Courier', 0xff7f7f00, 10, None)
        Text = ('Courier', 0xffffffff, 10, None)
    
    class VHDL:
        Attribute = ('Courier', 0xff804020, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentLine = ('Courier', 0xff3f7f3f, 10, None)
        Default = ('Courier', 0xff800080, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet7 = ('Courier', 0xff804020, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        StandardFunction = ('Courier', 0xff808020, 10, None)
        StandardOperator = ('Courier', 0xff74ccf4, 10, None)
        StandardPackage = ('Courier', 0xff208020, 10, None)
        StandardType = ('Courier', 0xff208080, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
    
    class Verilog:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentBang = ('Courier', 0xff3f7f3f, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Identifier = ('Courier', 0xffffffff, 10, None)
        Keyword = ('Courier', 0xff2389da, 10, None)
        KeywordSet2 = ('Courier', 0xff74ccf4, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xff007070, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        SystemTask = ('Courier', 0xff804020, 10, None)
        UnclosedString = ('Courier', 0xffffffff, 10, None)
        UserKeywordSet = ('Courier', 0xff2a00ff, 10, None)
    
    class XML:
        ASPAtStart = ('Courier', 0xffffffff, 10, None)
        ASPJavaScriptComment = ('Courier', 0xff6cab9d, 10, None)
        ASPJavaScriptCommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        ASPJavaScriptCommentLine = ('Courier', 0xff6cab9d, 10, None)
        ASPJavaScriptDefault = ('Courier', 0xffffffff, 10, None)
        ASPJavaScriptDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPJavaScriptKeyword = ('Courier', 0xff2389da, 10, None)
        ASPJavaScriptNumber = ('Courier', 0xff74ccf4, 10, None)
        ASPJavaScriptRegex = ('Courier', 0xffffffff, 10, None)
        ASPJavaScriptSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPJavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        ASPJavaScriptSymbol = ('Courier', 0xffffffff, 10, None)
        ASPJavaScriptUnclosedString = ('Courier', 0xffffffff, 10, None)
        ASPJavaScriptWord = ('Courier', 0xffffffff, 10, None)
        ASPPythonClassName = ('Courier', 0xff5abcd8, 10, None)
        ASPPythonComment = ('Courier', 0xff6cab9d, 10, None)
        ASPPythonDefault = ('Courier', 0xff808080, 10, None)
        ASPPythonDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPPythonFunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        ASPPythonIdentifier = ('Courier', 0xffffffff, 10, None)
        ASPPythonKeyword = ('Courier', 0xff2389da, 10, None)
        ASPPythonNumber = ('Courier', 0xff74ccf4, 10, None)
        ASPPythonOperator = ('Courier', 0xffffffff, 10, None)
        ASPPythonSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPPythonStart = ('Courier', 0xff808080, 10, None)
        ASPPythonTripleDoubleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        ASPPythonTripleSingleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        ASPStart = ('Courier', 0xffffffff, 10, None)
        ASPVBScriptComment = ('Courier', 0xff008000, 10, None)
        ASPVBScriptDefault = ('Courier', 0xffffffff, 10, None)
        ASPVBScriptIdentifier = ('Courier', 0xff1f76e4, 10, None)
        ASPVBScriptKeyword = ('Courier', 0xff1f76e4, 10, None)
        ASPVBScriptNumber = ('Courier', 0xff008080, 10, None)
        ASPVBScriptStart = ('Courier', 0xffffffff, 10, None)
        ASPVBScriptString = ('Courier', 0xff800080, 10, None)
        ASPVBScriptUnclosedString = ('Courier', 0xff1f76e4, 10, None)
        ASPXCComment = ('Courier', 0xffffffff, 10, None)
        Attribute = ('Courier', 0xff008080, 10, None)
        CDATA = ('Courier', 0xffedff86, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        Entity = ('Courier', 0xff800080, 10, None)
        HTMLComment = ('Courier', 0xff808000, 10, None)
        HTMLDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        HTMLNumber = ('Courier', 0xff74ccf4, 10, None)
        HTMLSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        HTMLValue = ('Courier', 0xff608060, 10, None)
        JavaScriptComment = ('Courier', 0xff6cab9d, 10, None)
        JavaScriptCommentDoc = ('Courier', 0xff3f703f, 10, None)
        JavaScriptCommentLine = ('Courier', 0xff6cab9d, 10, None)
        JavaScriptDefault = ('Courier', 0xffffffff, 10, None)
        JavaScriptDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        JavaScriptKeyword = ('Courier', 0xff2389da, 10, None)
        JavaScriptNumber = ('Courier', 0xff74ccf4, 10, None)
        JavaScriptRegex = ('Courier', 0xffffffff, 10, None)
        JavaScriptSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        JavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        JavaScriptSymbol = ('Courier', 0xffffffff, 10, None)
        JavaScriptUnclosedString = ('Courier', 0xffffffff, 10, None)
        JavaScriptWord = ('Courier', 0xffffffff, 10, None)
        OtherInTag = ('Courier', 0xff800080, 10, None)
        PHPComment = ('Courier', 0xff999999, 10, None)
        PHPCommentLine = ('Courier', 0xff666666, 10, None)
        PHPDefault = ('Courier', 0xffc7dbf5, 10, None)
        PHPDoubleQuotedString = ('Courier', 0xff6cab9d, 10, None)
        PHPDoubleQuotedVariable = ('Courier', 0xff2389da, 10, None)
        PHPKeyword = ('Courier', 0xffc4bbb8, 10, None)
        PHPNumber = ('Courier', 0xffcc9900, 10, None)
        PHPOperator = ('Courier', 0xffffffff, 10, None)
        PHPSingleQuotedString = ('Courier', 0xff009f00, 10, None)
        PHPStart = ('Courier', 0xffedff86, 10, None)
        PHPVariable = ('Courier', 0xff2389da, 10, None)
        PythonClassName = ('Courier', 0xff5abcd8, 10, None)
        PythonComment = ('Courier', 0xff6cab9d, 10, None)
        PythonDefault = ('Courier', 0xff808080, 10, None)
        PythonDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        PythonFunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        PythonIdentifier = ('Courier', 0xffffffff, 10, None)
        PythonKeyword = ('Courier', 0xff2389da, 10, None)
        PythonNumber = ('Courier', 0xff74ccf4, 10, None)
        PythonOperator = ('Courier', 0xffffffff, 10, None)
        PythonSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        PythonStart = ('Courier', 0xff808080, 10, None)
        PythonTripleDoubleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        PythonTripleSingleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        SGMLBlockDefault = ('Courier', 0xfffff5b2, 10, None)
        SGMLCommand = ('Courier', 0xff1f76e4, 10, None)
        SGMLComment = ('Courier', 0xff808000, 10, None)
        SGMLDefault = ('Courier', 0xff1f76e4, 10, None)
        SGMLDoubleQuotedString = ('Courier', 0xffedff86, 10, None)
        SGMLEntity = ('Courier', 0xff333333, 10, None)
        SGMLError = ('Courier', 0xffedff86, 10, None)
        SGMLParameter = ('Courier', 0xff006600, 10, None)
        SGMLParameterComment = ('Courier', 0xffffffff, 10, None)
        SGMLSingleQuotedString = ('Courier', 0xff993300, 10, None)
        SGMLSpecial = ('Courier', 0xff3366ff, 10, None)
        Script = ('Courier', 0xff1f76e4, 10, None)
        Tag = ('Courier', 0xff1f76e4, 10, None)
        UnknownAttribute = ('Courier', 0xff008080, 10, None)
        UnknownTag = ('Courier', 0xff1f76e4, 10, None)
        VBScriptComment = ('Courier', 0xff008000, 10, None)
        VBScriptDefault = ('Courier', 0xffffffff, 10, None)
        VBScriptIdentifier = ('Courier', 0xff1f76e4, 10, None)
        VBScriptKeyword = ('Courier', 0xff1f76e4, 10, None)
        VBScriptNumber = ('Courier', 0xff008080, 10, None)
        VBScriptStart = ('Courier', 0xffffffff, 10, None)
        VBScriptString = ('Courier', 0xff800080, 10, None)
        VBScriptUnclosedString = ('Courier', 0xff1f76e4, 10, None)
        XMLEnd = ('Courier', 0xff800080, 10, None)
        XMLStart = ('Courier', 0xff800080, 10, None)
        XMLTagEnd = ('Courier', 0xff1f76e4, 10, None)
    
    class YAML:
        Comment = ('Courier', 0xff008800, 10, None)
        Default = ('Courier', 0xffffffff, 10, None)
        DocumentDelimiter = ('Courier', 0xff112435, 10, None)
        Identifier = ('Courier', 0xfff3c969, 10, None)
        Keyword = ('Courier', 0xff880088, 10, None)
        Number = ('Courier', 0xff880000, 10, None)
        Operator = ('Courier', 0xffffffff, 10, None)
        Reference = ('Courier', 0xff008888, 10, None)
        SyntaxErrorMarker = ('Courier', 0xff112435, 10, None)
        TextBlockMarker = ('Courier', 0xff333366, 10, None)


class Paper:
    Default = PyQt4.QtGui.QColor(0xff112435)
    
    class Ada:
        Default = 0xff112435
        Comment = 0xff112435
        Keyword = 0xff112435
        String = 0xff112435
        Procedure = 0xff112435
        Number = 0xff112435
        Type = 0xff112435
        Package = 0xff112435
    
    class Nim:
        Default = 0xff112435
        Comment = 0xff112435
        BasicKeyword = 0xff112435
        TopKeyword = 0xff112435
        String = 0xff112435
        LongString = 0xff112435
        Number = 0xff112435
        Operator = 0xff112435
        Unsafe = 0xff112435
        Type = 0xff112435
        DocumentationComment = 0xff112435
        Definition = 0xff112435
        Class = 0xff112435
        KeywordOperator = 0xff112435
        CharLiteral = 0xff112435
        CaseOf = 0xff112435
        UserKeyword = 0xff112435
        MultilineComment = 0xff112435
        MultilineDocumentation = 0xff112435
        Pragma = 0xff112435
    
    class Oberon:
        Default = 0xff112435
        Comment = 0xff112435
        Keyword = 0xff112435
        String = 0xff112435
        Procedure = 0xff112435
        Module = 0xff112435
        Number = 0xff112435
        Type = 0xff112435
    
    
    # Generated
    class AVS:
        Function = 0xff112435
        KeywordSet6 = 0xff112435
        TripleString = 0xff112435
        LineComment = 0xff112435
        Plugin = 0xff112435
        String = 0xff112435
        ClipProperty = 0xff112435
        Default = 0xff112435
        Operator = 0xff112435
        Number = 0xff112435
        Filter = 0xff112435
        Identifier = 0xff112435
        NestedBlockComment = 0xff112435
        Keyword = 0xff112435
        BlockComment = 0xff112435
    
    class Bash:
        Error = 0xffff0000
        Backticks = 0xffa08080
        SingleQuotedHereDocument = 0xffddd0dd
        Scalar = 0xffffe0e0
        HereDocumentDelimiter = 0xffddd0dd
        Comment = 0xff112435
        SingleQuotedString = 0xff112435
        Default = 0xff112435
        Operator = 0xff112435
        ParameterExpansion = 0xffffffe0
        Number = 0xff112435
        Identifier = 0xff112435
        Keyword = 0xff112435
        DoubleQuotedString = 0xff112435
    
    class Batch:
        Label = 0xff606060
        Default = 0xff112435
        Keyword = 0xff112435
        ExternalCommand = 0xff112435
        Variable = 0xff112435
        Comment = 0xff112435
        HideCommandChar = 0xff112435
        Operator = 0xff112435
    
    class CMake:
        Function = 0xff112435
        BlockForeach = 0xff112435
        BlockWhile = 0xff112435
        StringLeftQuote = 0xffeeeeee
        Label = 0xff112435
        Comment = 0xff112435
        BlockMacro = 0xff112435
        StringRightQuote = 0xffeeeeee
        Default = 0xff112435
        Number = 0xff112435
        BlockIf = 0xff112435
        Variable = 0xff112435
        KeywordSet3 = 0xff112435
        String = 0xffeeeeee
        StringVariable = 0xffeeeeee
    
    class CPP:
        CommentDocKeywordError = 0xff112435
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff112435
        UUID = 0xff112435
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff112435
        Operator = 0xff112435
        InactiveOperator = 0xff112435
        InactivePreProcessor = 0xff112435
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff112435
        InactiveRawString = 0xff112435
        PreProcessor = 0xff112435
        KeywordSet2 = 0xff112435
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xff112435
        InactiveNumber = 0xff112435
        InactivePreProcessorCommentLineDoc = 0xff112435
        Number = 0xff112435
        InactiveUUID = 0xff112435
        CommentDoc = 0xff112435
        InactiveCommentDoc = 0xff112435
        GlobalClass = 0xff112435
        InactiveSingleQuotedString = 0xff112435
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff112435
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xff112435
        InactiveIdentifier = 0xff112435
        CommentLineDoc = 0xff112435
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xff112435
        InactiveCommentDocKeyword = 0xff112435
        Keyword = 0xff112435
        InactiveCommentLineDoc = 0xff112435
        InactiveDefault = 0xff112435
        InactiveCommentDocKeywordError = 0xff112435
        InactiveTripleQuotedVerbatimString = 0xff112435
        CommentDocKeyword = 0xff112435
        InactiveDoubleQuotedString = 0xff112435
        CommentLine = 0xff112435
        Comment = 0xff112435
        PreProcessorComment = 0xff112435
        InactiveComment = 0xff112435
        RawString = 0xfffff3ff
        Default = 0xff112435
        PreProcessorCommentLineDoc = 0xff112435
        DoubleQuotedString = 0xff112435
        InactiveKeyword = 0xff112435
    
    class CSS:
        Important = 0xff112435
        CSS3Property = 0xff112435
        Attribute = 0xff112435
        Comment = 0xff112435
        SingleQuotedString = 0xff112435
        MediaRule = 0xff112435
        AtRule = 0xff112435
        UnknownPseudoClass = 0xff112435
        PseudoClass = 0xff112435
        Tag = 0xff112435
        CSS2Property = 0xff112435
        CSS1Property = 0xff112435
        IDSelector = 0xff112435
        ExtendedCSSProperty = 0xff112435
        Variable = 0xff112435
        ExtendedPseudoClass = 0xff112435
        ClassSelector = 0xff112435
        Default = 0xff112435
        PseudoElement = 0xff112435
        UnknownProperty = 0xff112435
        Value = 0xff112435
        ExtendedPseudoElement = 0xff112435
        DoubleQuotedString = 0xff112435
        Operator = 0xff112435
    
    class CSharp:
        CommentDocKeywordError = 0xff112435
        InactiveRegex = 0xff112435
        InactivePreProcessorComment = 0xff112435
        UUID = 0xff112435
        InactiveVerbatimString = 0xff112435
        SingleQuotedString = 0xff112435
        Operator = 0xff112435
        InactiveOperator = 0xff112435
        InactivePreProcessor = 0xff112435
        UnclosedString = 0xff112435
        Identifier = 0xff112435
        InactiveRawString = 0xff112435
        PreProcessor = 0xff112435
        KeywordSet2 = 0xff112435
        InactiveUnclosedString = 0xff112435
        InactiveCommentLine = 0xff112435
        InactiveNumber = 0xff112435
        InactivePreProcessorCommentLineDoc = 0xff112435
        Number = 0xff112435
        InactiveUUID = 0xff112435
        CommentDoc = 0xff112435
        InactiveCommentDoc = 0xff112435
        GlobalClass = 0xff112435
        InactiveSingleQuotedString = 0xff112435
        HashQuotedString = 0xff112435
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff112435
        Regex = 0xff112435
        InactiveGlobalClass = 0xff112435
        InactiveIdentifier = 0xff112435
        CommentLineDoc = 0xff112435
        TripleQuotedVerbatimString = 0xff112435
        InactiveKeywordSet2 = 0xff112435
        InactiveCommentDocKeyword = 0xff112435
        Keyword = 0xff112435
        InactiveCommentLineDoc = 0xff112435
        InactiveDefault = 0xff112435
        InactiveCommentDocKeywordError = 0xff112435
        InactiveTripleQuotedVerbatimString = 0xff112435
        CommentDocKeyword = 0xff112435
        InactiveDoubleQuotedString = 0xff112435
        CommentLine = 0xff112435
        Comment = 0xff112435
        PreProcessorComment = 0xff112435
        InactiveComment = 0xff112435
        RawString = 0xff112435
        Default = 0xff112435
        PreProcessorCommentLineDoc = 0xff112435
        DoubleQuotedString = 0xff112435
        InactiveKeyword = 0xff112435
    
    class CoffeeScript:
        UUID = 0xff112435
        CommentDocKeywordError = 0xff112435
        GlobalClass = 0xff112435
        VerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff112435
        Operator = 0xff112435
        Number = 0xff112435
        Identifier = 0xff112435
        Keyword = 0xff112435
        UnclosedString = 0xffe0c0e0
        Regex = 0xffe0f0e0
        CommentDocKeyword = 0xff112435
        BlockRegex = 0xff112435
        CommentLineDoc = 0xff112435
        PreProcessor = 0xff112435
        CommentLine = 0xff112435
        CommentBlock = 0xff112435
        Comment = 0xff112435
        KeywordSet2 = 0xff112435
        BlockRegexComment = 0xff112435
        Default = 0xff112435
        DoubleQuotedString = 0xff112435
        CommentDoc = 0xff112435
    
    class D:
        BackquoteString = 0xff112435
        CommentDocKeywordError = 0xff112435
        Operator = 0xff112435
        CommentNested = 0xff112435
        KeywordDoc = 0xff112435
        KeywordSet7 = 0xff112435
        Keyword = 0xff112435
        KeywordSecondary = 0xff112435
        Identifier = 0xff112435
        KeywordSet5 = 0xff112435
        CommentDocKeyword = 0xff112435
        KeywordSet6 = 0xff112435
        CommentLineDoc = 0xff112435
        CommentLine = 0xff112435
        Comment = 0xff112435
        Typedefs = 0xff112435
        Character = 0xff112435
        RawString = 0xff112435
        Default = 0xff112435
        Number = 0xff112435
        UnclosedString = 0xffe0c0e0
        String = 0xff112435
        CommentDoc = 0xff112435
    
    class Diff:
        Header = 0xff112435
        LineChanged = 0xff112435
        Default = 0xff112435
        LineRemoved = 0xff112435
        Command = 0xff112435
        Position = 0xff112435
        LineAdded = 0xff112435
        Comment = 0xff112435
    
    class Fortran:
        Label = 0xff112435
        Identifier = 0xff112435
        DottedOperator = 0xff112435
        PreProcessor = 0xff112435
        Comment = 0xff112435
        SingleQuotedString = 0xff112435
        Default = 0xff112435
        DoubleQuotedString = 0xff112435
        ExtendedFunction = 0xff112435
        UnclosedString = 0xffe0c0e0
        Number = 0xff112435
        Continuation = 0xfff0e080
        IntrinsicFunction = 0xff112435
        Keyword = 0xff112435
        Operator = 0xff112435
    
    class Fortran77:
        Label = 0xff112435
        Identifier = 0xff112435
        DottedOperator = 0xff112435
        PreProcessor = 0xff112435
        Comment = 0xff112435
        SingleQuotedString = 0xff112435
        Default = 0xff112435
        DoubleQuotedString = 0xff112435
        ExtendedFunction = 0xff112435
        UnclosedString = 0xffe0c0e0
        Number = 0xff112435
        Continuation = 0xfff0e080
        IntrinsicFunction = 0xff112435
        Keyword = 0xff112435
        Operator = 0xff112435
    
    class HTML:
        HTMLValue = 0xffffefff
        PythonDefault = 0xffefffef
        Entity = 0xff112435
        SGMLParameter = 0xffefefff
        SGMLDefault = 0xffefefff
        PHPVariable = 0xfffff8f8
        SGMLCommand = 0xffefefff
        PythonClassName = 0xffefffef
        VBScriptUnclosedString = 0xff7f7fff
        ASPJavaScriptDefault = 0xffdfdf7f
        ASPVBScriptStart = 0xff112435
        VBScriptDefault = 0xffefefff
        PythonNumber = 0xffefffef
        PythonOperator = 0xffefffef
        ASPJavaScriptSingleQuotedString = 0xffdfdf7f
        PHPDefault = 0xfffff8f8
        XMLStart = 0xff112435
        PythonFunctionMethodName = 0xffefffef
        ASPJavaScriptStart = 0xff112435
        JavaScriptWord = 0xfff0f0ff
        PHPSingleQuotedString = 0xfffff8f8
        PythonTripleDoubleQuotedString = 0xffefffef
        JavaScriptComment = 0xfff0f0ff
        Default = 0xff112435
        SGMLSingleQuotedString = 0xffefefff
        VBScriptComment = 0xffefefff
        ASPVBScriptNumber = 0xffcfcfef
        ASPJavaScriptCommentDoc = 0xffdfdf7f
        PythonIdentifier = 0xffefffef
        VBScriptKeyword = 0xffefefff
        JavaScriptDefault = 0xfff0f0ff
        PythonStart = 0xff112435
        ASPPythonComment = 0xffcfefcf
        ASPJavaScriptWord = 0xffdfdf7f
        SGMLParameterComment = 0xff112435
        JavaScriptSingleQuotedString = 0xfff0f0ff
        PythonSingleQuotedString = 0xffefffef
        HTMLSingleQuotedString = 0xff112435
        ASPVBScriptString = 0xffcfcfef
        SGMLBlockDefault = 0xffcccce0
        PythonKeyword = 0xffefffef
        XMLTagEnd = 0xff112435
        ASPVBScriptComment = 0xffcfcfef
        ASPPythonSingleQuotedString = 0xffcfefcf
        PHPDoubleQuotedVariable = 0xfffff8f8
        ASPJavaScriptComment = 0xffdfdf7f
        JavaScriptUnclosedString = 0xffbfbbb0
        JavaScriptDoubleQuotedString = 0xfff0f0ff
        UnknownAttribute = 0xff112435
        ASPPythonOperator = 0xffcfefcf
        ASPJavaScriptSymbol = 0xffdfdf7f
        ASPPythonFunctionMethodName = 0xffcfefcf
        SGMLDoubleQuotedString = 0xffefefff
        PHPOperator = 0xfffff8f8
        JavaScriptNumber = 0xfff0f0ff
        PythonDoubleQuotedString = 0xffefffef
        ASPAtStart = 0xffffff00
        Script = 0xff112435
        PHPCommentLine = 0xfffff8f8
        SGMLComment = 0xffefefff
        JavaScriptStart = 0xff112435
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
        OtherInTag = 0xff112435
        JavaScriptCommentDoc = 0xfff0f0ff
        Tag = 0xff112435
        XMLEnd = 0xff112435
        CDATA = 0xffffdf00
        HTMLNumber = 0xff112435
        SGMLError = 0xffff6666
        PHPKeyword = 0xfffff8f8
        ASPVBScriptUnclosedString = 0xff7f7fff
        ASPPythonNumber = 0xffcfefcf
        VBScriptString = 0xffefefff
        ASPPythonClassName = 0xffcfefcf
        ASPPythonStart = 0xff112435
        JavaScriptRegex = 0xffffbbb0
        ASPJavaScriptUnclosedString = 0xffbfbbb0
        ASPJavaScriptCommentLine = 0xffdfdf7f
        SGMLEntity = 0xffefefff
        ASPJavaScriptDoubleQuotedString = 0xffdfdf7f
        ASPStart = 0xffffdf00
        Attribute = 0xff112435
        ASPJavaScriptKeyword = 0xffdfdf7f
        ASPVBScriptDefault = 0xffcfcfef
        ASPVBScriptIdentifier = 0xffcfcfef
        ASPJavaScriptRegex = 0xffffbbb0
        VBScriptNumber = 0xffefefff
        HTMLDoubleQuotedString = 0xff112435
        ASPXCComment = 0xff112435
        VBScriptStart = 0xff112435
        PHPDoubleQuotedString = 0xfffff8f8
        PHPComment = 0xfffff8f8
        ASPPythonTripleSingleQuotedString = 0xffcfefcf
        ASPPythonDoubleQuotedString = 0xffcfefcf
        JavaScriptKeyword = 0xfff0f0ff
        JavaScriptSymbol = 0xfff0f0ff
        VBScriptIdentifier = 0xffefefff
        HTMLComment = 0xff112435
        UnknownTag = 0xff112435
        JavaScriptCommentLine = 0xfff0f0ff
        PythonComment = 0xffefffef
    
    class IDL:
        CommentDocKeywordError = 0xff112435
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff112435
        UUID = 0xff112435
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff112435
        Operator = 0xff112435
        InactiveOperator = 0xff112435
        InactivePreProcessor = 0xff112435
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff112435
        InactiveRawString = 0xff112435
        PreProcessor = 0xff112435
        KeywordSet2 = 0xff112435
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xff112435
        InactiveNumber = 0xff112435
        InactivePreProcessorCommentLineDoc = 0xff112435
        Number = 0xff112435
        InactiveUUID = 0xff112435
        CommentDoc = 0xff112435
        InactiveCommentDoc = 0xff112435
        GlobalClass = 0xff112435
        InactiveSingleQuotedString = 0xff112435
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff112435
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xff112435
        InactiveIdentifier = 0xff112435
        CommentLineDoc = 0xff112435
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xff112435
        InactiveCommentDocKeyword = 0xff112435
        Keyword = 0xff112435
        InactiveCommentLineDoc = 0xff112435
        InactiveDefault = 0xff112435
        InactiveCommentDocKeywordError = 0xff112435
        InactiveTripleQuotedVerbatimString = 0xff112435
        CommentDocKeyword = 0xff112435
        InactiveDoubleQuotedString = 0xff112435
        CommentLine = 0xff112435
        Comment = 0xff112435
        PreProcessorComment = 0xff112435
        InactiveComment = 0xff112435
        RawString = 0xfffff3ff
        Default = 0xff112435
        PreProcessorCommentLineDoc = 0xff112435
        DoubleQuotedString = 0xff112435
        InactiveKeyword = 0xff112435
    
    class Java:
        CommentDocKeywordError = 0xff112435
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff112435
        UUID = 0xff112435
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff112435
        Operator = 0xff112435
        InactiveOperator = 0xff112435
        InactivePreProcessor = 0xff112435
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff112435
        InactiveRawString = 0xff112435
        PreProcessor = 0xff112435
        KeywordSet2 = 0xff112435
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xff112435
        InactiveNumber = 0xff112435
        InactivePreProcessorCommentLineDoc = 0xff112435
        Number = 0xff112435
        InactiveUUID = 0xff112435
        CommentDoc = 0xff112435
        InactiveCommentDoc = 0xff112435
        GlobalClass = 0xff112435
        InactiveSingleQuotedString = 0xff112435
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff112435
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xff112435
        InactiveIdentifier = 0xff112435
        CommentLineDoc = 0xff112435
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xff112435
        InactiveCommentDocKeyword = 0xff112435
        Keyword = 0xff112435
        InactiveCommentLineDoc = 0xff112435
        InactiveDefault = 0xff112435
        InactiveCommentDocKeywordError = 0xff112435
        InactiveTripleQuotedVerbatimString = 0xff112435
        CommentDocKeyword = 0xff112435
        InactiveDoubleQuotedString = 0xff112435
        CommentLine = 0xff112435
        Comment = 0xff112435
        PreProcessorComment = 0xff112435
        InactiveComment = 0xff112435
        RawString = 0xfffff3ff
        Default = 0xff112435
        PreProcessorCommentLineDoc = 0xff112435
        DoubleQuotedString = 0xff112435
        InactiveKeyword = 0xff112435
    
    class JavaScript:
        CommentDocKeywordError = 0xff112435
        InactiveRegex = 0xff112435
        InactivePreProcessorComment = 0xff112435
        UUID = 0xff112435
        InactiveVerbatimString = 0xff112435
        SingleQuotedString = 0xff112435
        Operator = 0xff112435
        InactiveOperator = 0xff112435
        InactivePreProcessor = 0xff112435
        UnclosedString = 0xff112435
        Identifier = 0xff112435
        InactiveRawString = 0xff112435
        PreProcessor = 0xff112435
        KeywordSet2 = 0xff112435
        InactiveUnclosedString = 0xff112435
        InactiveCommentLine = 0xff112435
        InactiveNumber = 0xff112435
        InactivePreProcessorCommentLineDoc = 0xff112435
        Number = 0xff112435
        InactiveUUID = 0xff112435
        CommentDoc = 0xff112435
        InactiveCommentDoc = 0xff112435
        GlobalClass = 0xff112435
        InactiveSingleQuotedString = 0xff112435
        HashQuotedString = 0xff112435
        VerbatimString = 0xff112435
        InactiveHashQuotedString = 0xff112435
        Regex = 0xffe0f0ff
        InactiveGlobalClass = 0xff112435
        InactiveIdentifier = 0xff112435
        CommentLineDoc = 0xff112435
        TripleQuotedVerbatimString = 0xff112435
        InactiveKeywordSet2 = 0xff112435
        InactiveCommentDocKeyword = 0xff112435
        Keyword = 0xff112435
        InactiveCommentLineDoc = 0xff112435
        InactiveDefault = 0xff112435
        InactiveCommentDocKeywordError = 0xff112435
        InactiveTripleQuotedVerbatimString = 0xff112435
        CommentDocKeyword = 0xff112435
        InactiveDoubleQuotedString = 0xff112435
        CommentLine = 0xff112435
        Comment = 0xff112435
        PreProcessorComment = 0xff112435
        InactiveComment = 0xff112435
        RawString = 0xff112435
        Default = 0xff112435
        PreProcessorCommentLineDoc = 0xff112435
        DoubleQuotedString = 0xff112435
        InactiveKeyword = 0xff112435
    
    class Lua:
        Label = 0xff112435
        Identifier = 0xff112435
        StringTableMathsFunctions = 0xffd0d0ff
        CoroutinesIOSystemFacilities = 0xffffd0d0
        KeywordSet5 = 0xff112435
        KeywordSet6 = 0xff112435
        Preprocessor = 0xff112435
        LineComment = 0xff112435
        Comment = 0xffd0f0f0
        String = 0xff112435
        Character = 0xff112435
        Default = 0xff112435
        Operator = 0xff112435
        LiteralString = 0xffe0ffff
        Number = 0xff112435
        KeywordSet8 = 0xff112435
        KeywordSet7 = 0xff112435
        BasicFunctions = 0xffd0ffd0
        Keyword = 0xff112435
        UnclosedString = 0xffe0c0e0
    
    class Makefile:
        Default = 0xff112435
        Operator = 0xff112435
        Target = 0xff112435
        Preprocessor = 0xff112435
        Variable = 0xff112435
        Comment = 0xff112435
        Error = 0xffff0000
    
    class Matlab:
        SingleQuotedString = 0xff112435
        Default = 0xff112435
        Keyword = 0xff112435
        Number = 0xff112435
        Command = 0xff112435
        Identifier = 0xff112435
        Comment = 0xff112435
        DoubleQuotedString = 0xff112435
        Operator = 0xff112435
    
    class Octave:
        SingleQuotedString = 0xff112435
        Default = 0xff112435
        Keyword = 0xff112435
        Number = 0xff112435
        Command = 0xff112435
        Identifier = 0xff112435
        Comment = 0xff112435
        DoubleQuotedString = 0xff112435
        Operator = 0xff112435
    
    class PO:
        ProgrammerComment = 0xff112435
        Flags = 0xff112435
        MessageContextText = 0xff112435
        MessageStringTextEOL = 0xff112435
        MessageId = 0xff112435
        MessageIdText = 0xff112435
        Reference = 0xff112435
        Comment = 0xff112435
        MessageStringText = 0xff112435
        MessageContext = 0xff112435
        Fuzzy = 0xff112435
        Default = 0xff112435
        MessageString = 0xff112435
        MessageContextTextEOL = 0xff112435
        MessageIdTextEOL = 0xff112435
    
    class POV:
        KeywordSet7 = 0xffd0d0d0
        KeywordSet6 = 0xffd0ffd0
        PredefinedFunctions = 0xffd0d0ff
        CommentLine = 0xff112435
        PredefinedIdentifiers = 0xff112435
        Comment = 0xff112435
        Directive = 0xff112435
        String = 0xff112435
        BadDirective = 0xff112435
        TypesModifiersItems = 0xffffffd0
        Default = 0xff112435
        Operator = 0xff112435
        Number = 0xff112435
        KeywordSet8 = 0xffe0e0e0
        Identifier = 0xff112435
        ObjectsCSGAppearance = 0xffffd0d0
        UnclosedString = 0xffe0c0e0
    
    class Pascal:
        PreProcessorParenthesis = 0xff112435
        SingleQuotedString = 0xff112435
        PreProcessor = 0xff112435
        CommentLine = 0xff112435
        Comment = 0xff112435
        CommentParenthesis = 0xff112435
        Asm = 0xff112435
        Character = 0xff112435
        Default = 0xff112435
        Operator = 0xff112435
        UnclosedString = 0xffe0c0e0
        Number = 0xff112435
        Identifier = 0xff112435
        Keyword = 0xff112435
        HexNumber = 0xff112435
    
    class Perl:
        Translation = 0xfff0e080
        BacktickHereDocument = 0xffddd0dd
        Array = 0xffffffe0
        QuotedStringQXVar = 0xffa08080
        PODVerbatim = 0xffc0ffc0
        DoubleQuotedStringVar = 0xff112435
        Regex = 0xffa0ffa0
        HereDocumentDelimiter = 0xffddd0dd
        SubroutinePrototype = 0xff112435
        BacktickHereDocumentVar = 0xffddd0dd
        QuotedStringQR = 0xff112435
        SingleQuotedString = 0xff112435
        QuotedStringQRVar = 0xff112435
        SubstitutionVar = 0xff112435
        Operator = 0xff112435
        DoubleQuotedHereDocumentVar = 0xffddd0dd
        Identifier = 0xff112435
        QuotedStringQX = 0xff112435
        BackticksVar = 0xffa08080
        Keyword = 0xff112435
        QuotedStringQ = 0xff112435
        QuotedStringQQVar = 0xff112435
        QuotedStringQQ = 0xff112435
        POD = 0xffe0ffe0
        FormatIdentifier = 0xff112435
        RegexVar = 0xff112435
        Backticks = 0xffa08080
        DoubleQuotedHereDocument = 0xffddd0dd
        Scalar = 0xffffe0e0
        FormatBody = 0xfffff0ff
        Comment = 0xff112435
        QuotedStringQW = 0xff112435
        SymbolTable = 0xffe0e0e0
        Default = 0xff112435
        Error = 0xffff0000
        SingleQuotedHereDocument = 0xffddd0dd
        Number = 0xff112435
        Hash = 0xffffe0ff
        Substitution = 0xfff0e080
        DataSection = 0xfffff0d8
        DoubleQuotedString = 0xff112435
    
    class PostScript:
        DictionaryParenthesis = 0xff112435
        HexString = 0xff112435
        DSCCommentValue = 0xff112435
        ProcedureParenthesis = 0xff112435
        Comment = 0xff112435
        ImmediateEvalLiteral = 0xff112435
        Name = 0xff112435
        DSCComment = 0xff112435
        Default = 0xff112435
        Base85String = 0xff112435
        Number = 0xff112435
        ArrayParenthesis = 0xff112435
        Literal = 0xff112435
        BadStringCharacter = 0xffff0000
        Text = 0xff112435
        Keyword = 0xff112435
    
    class Properties:
        DefaultValue = 0xff112435
        Default = 0xff112435
        Section = 0xffe0f0f0
        Assignment = 0xff112435
        Key = 0xff112435
        Comment = 0xff112435
    
    class Python:
        TripleDoubleQuotedString = 0xff112435
        FunctionMethodName = 0xff112435
        TabsAfterSpaces = 0xff112435
        Tabs = 0xff112435
        Decorator = 0xff112435
        NoWarning = 0xff112435
        UnclosedString = 0xffe0c0e0
        Spaces = 0xff112435
        CommentBlock = 0xff112435
        Comment = 0xff112435
        TripleSingleQuotedString = 0xff112435
        SingleQuotedString = 0xff112435
        Inconsistent = 0xff112435
        Default = 0xff112435
        DoubleQuotedString = 0xff112435
        Operator = 0xff112435
        Number = 0xff112435
        Identifier = 0xff112435
        ClassName = 0xff112435
        Keyword = 0xff112435
        HighlightedIdentifier = 0xff112435
    
    class Ruby:
        Symbol = 0xff112435
        Stderr = 0xffff8080
        Global = 0xff112435
        FunctionMethodName = 0xff112435
        Stdin = 0xffff8080
        HereDocumentDelimiter = 0xffddd0dd
        PercentStringr = 0xffa0ffa0
        PercentStringQ = 0xff112435
        ModuleName = 0xff112435
        HereDocument = 0xffddd0dd
        SingleQuotedString = 0xff112435
        PercentStringq = 0xff112435
        Regex = 0xffa0ffa0
        Operator = 0xff112435
        PercentStringw = 0xffffffe0
        PercentStringx = 0xffa08080
        POD = 0xffc0ffc0
        Keyword = 0xff112435
        Stdout = 0xffff8080
        ClassVariable = 0xff112435
        Identifier = 0xff112435
        DemotedKeyword = 0xff112435
        Backticks = 0xffa08080
        InstanceVariable = 0xff112435
        Comment = 0xff112435
        Default = 0xff112435
        Error = 0xffff0000
        Number = 0xff112435
        DataSection = 0xfffff0d8
        ClassName = 0xff112435
        DoubleQuotedString = 0xff112435
    
    class SQL:
        PlusComment = 0xff112435
        KeywordSet7 = 0xff112435
        PlusPrompt = 0xffe0ffe0
        CommentDocKeywordError = 0xff112435
        CommentDocKeyword = 0xff112435
        KeywordSet6 = 0xff112435
        CommentLine = 0xff112435
        Comment = 0xff112435
        Operator = 0xff112435
        QuotedIdentifier = 0xff112435
        SingleQuotedString = 0xff112435
        PlusKeyword = 0xff112435
        Default = 0xff112435
        DoubleQuotedString = 0xff112435
        CommentLineHash = 0xff112435
        KeywordSet5 = 0xff112435
        Number = 0xff112435
        KeywordSet8 = 0xff112435
        Identifier = 0xff112435
        Keyword = 0xff112435
        CommentDoc = 0xff112435
    
    class Spice:
        Function = 0xff112435
        Delimiter = 0xff112435
        Value = 0xff112435
        Default = 0xff112435
        Number = 0xff112435
        Parameter = 0xff112435
        Command = 0xff112435
        Identifier = 0xff112435
        Comment = 0xff112435
    
    class TCL:
        SubstitutionBrace = 0xff112435
        CommentBox = 0xfff0fff0
        ITCLKeyword = 0xfffff0f0
        TkKeyword = 0xffe0fff0
        Operator = 0xff112435
        QuotedString = 0xfffff0f0
        ExpandKeyword = 0xffffff80
        KeywordSet7 = 0xff112435
        TCLKeyword = 0xff112435
        TkCommand = 0xffffd0d0
        Identifier = 0xff112435
        KeywordSet6 = 0xff112435
        CommentLine = 0xff112435
        CommentBlock = 0xfff0fff0
        Comment = 0xfff0ffe0
        Default = 0xff112435
        KeywordSet9 = 0xff112435
        Modifier = 0xff112435
        Number = 0xff112435
        KeywordSet8 = 0xff112435
        Substitution = 0xffeffff0
        QuotedKeyword = 0xfffff0f0
    
    class TeX:
        Symbol = 0xff112435
        Default = 0xff112435
        Command = 0xff112435
        Group = 0xff112435
        Text = 0xff112435
        Special = 0xff112435
    
    class VHDL:
        StandardOperator = 0xff112435
        Attribute = 0xff112435
        CommentLine = 0xff112435
        Comment = 0xff112435
        String = 0xff112435
        Default = 0xff112435
        Operator = 0xff112435
        StandardPackage = 0xff112435
        Number = 0xff112435
        Identifier = 0xff112435
        KeywordSet7 = 0xff112435
        StandardFunction = 0xff112435
        StandardType = 0xff112435
        Keyword = 0xff112435
        UnclosedString = 0xffe0c0e0
    
    class Verilog:
        CommentBang = 0xffe0f0ff
        UserKeywordSet = 0xff112435
        Preprocessor = 0xff112435
        CommentLine = 0xff112435
        Comment = 0xff112435
        KeywordSet2 = 0xff112435
        Default = 0xff112435
        Operator = 0xff112435
        Number = 0xff112435
        Identifier = 0xff112435
        SystemTask = 0xff112435
        String = 0xff112435
        Keyword = 0xff112435
        UnclosedString = 0xffe0c0e0
    
    class XML:
        HTMLValue = 0xffffefff
        PythonDefault = 0xffefffef
        Entity = 0xff112435
        SGMLParameter = 0xffefefff
        SGMLDefault = 0xffefefff
        PHPVariable = 0xfffff8f8
        SGMLCommand = 0xffefefff
        PythonClassName = 0xffefffef
        VBScriptUnclosedString = 0xff7f7fff
        ASPJavaScriptDefault = 0xffdfdf7f
        ASPVBScriptStart = 0xff112435
        VBScriptDefault = 0xffefefff
        PythonNumber = 0xffefffef
        PythonOperator = 0xffefffef
        ASPJavaScriptSingleQuotedString = 0xffdfdf7f
        PHPDefault = 0xfffff8f8
        XMLStart = 0xff112435
        PythonFunctionMethodName = 0xffefffef
        ASPJavaScriptStart = 0xff112435
        JavaScriptWord = 0xfff0f0ff
        PHPSingleQuotedString = 0xfffff8f8
        PythonTripleDoubleQuotedString = 0xffefffef
        JavaScriptComment = 0xfff0f0ff
        Default = 0xff112435
        SGMLSingleQuotedString = 0xffefefff
        VBScriptComment = 0xffefefff
        ASPVBScriptNumber = 0xffcfcfef
        ASPJavaScriptCommentDoc = 0xffdfdf7f
        PythonIdentifier = 0xffefffef
        VBScriptKeyword = 0xffefefff
        JavaScriptDefault = 0xfff0f0ff
        PythonStart = 0xff112435
        ASPPythonComment = 0xffcfefcf
        ASPJavaScriptWord = 0xffdfdf7f
        SGMLParameterComment = 0xff112435
        JavaScriptSingleQuotedString = 0xfff0f0ff
        PythonSingleQuotedString = 0xffefffef
        HTMLSingleQuotedString = 0xff112435
        ASPVBScriptString = 0xffcfcfef
        SGMLBlockDefault = 0xffcccce0
        PythonKeyword = 0xffefffef
        XMLTagEnd = 0xff112435
        ASPVBScriptComment = 0xffcfcfef
        ASPPythonSingleQuotedString = 0xffcfefcf
        PHPDoubleQuotedVariable = 0xfffff8f8
        ASPJavaScriptComment = 0xffdfdf7f
        JavaScriptUnclosedString = 0xffbfbbb0
        JavaScriptDoubleQuotedString = 0xfff0f0ff
        UnknownAttribute = 0xff112435
        ASPPythonOperator = 0xffcfefcf
        ASPJavaScriptSymbol = 0xffdfdf7f
        ASPPythonFunctionMethodName = 0xffcfefcf
        SGMLDoubleQuotedString = 0xffefefff
        PHPOperator = 0xfffff8f8
        JavaScriptNumber = 0xfff0f0ff
        PythonDoubleQuotedString = 0xffefffef
        ASPAtStart = 0xffffff00
        Script = 0xff112435
        PHPCommentLine = 0xfffff8f8
        SGMLComment = 0xffefefff
        JavaScriptStart = 0xff112435
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
        OtherInTag = 0xff112435
        JavaScriptCommentDoc = 0xfff0f0ff
        Tag = 0xff112435
        XMLEnd = 0xff112435
        CDATA = 0xfffff0f0
        HTMLNumber = 0xff112435
        SGMLError = 0xffff6666
        PHPKeyword = 0xfffff8f8
        ASPVBScriptUnclosedString = 0xff7f7fff
        ASPPythonNumber = 0xffcfefcf
        VBScriptString = 0xffefefff
        ASPPythonClassName = 0xffcfefcf
        ASPPythonStart = 0xff112435
        JavaScriptRegex = 0xffffbbb0
        ASPJavaScriptUnclosedString = 0xffbfbbb0
        ASPJavaScriptCommentLine = 0xffdfdf7f
        SGMLEntity = 0xffefefff
        ASPJavaScriptDoubleQuotedString = 0xffdfdf7f
        ASPStart = 0xffffdf00
        Attribute = 0xff112435
        ASPJavaScriptKeyword = 0xffdfdf7f
        ASPVBScriptDefault = 0xffcfcfef
        ASPVBScriptIdentifier = 0xffcfcfef
        ASPJavaScriptRegex = 0xffffbbb0
        VBScriptNumber = 0xffefefff
        HTMLDoubleQuotedString = 0xff112435
        ASPXCComment = 0xff112435
        VBScriptStart = 0xff112435
        PHPDoubleQuotedString = 0xfffff8f8
        PHPComment = 0xfffff8f8
        ASPPythonTripleSingleQuotedString = 0xffcfefcf
        ASPPythonDoubleQuotedString = 0xffcfefcf
        JavaScriptKeyword = 0xfff0f0ff
        JavaScriptSymbol = 0xfff0f0ff
        VBScriptIdentifier = 0xffefefff
        HTMLComment = 0xff112435
        UnknownTag = 0xff112435
        JavaScriptCommentLine = 0xfff0f0ff
        PythonComment = 0xffefffef
    
    class YAML:
        TextBlockMarker = 0xff112435
        DocumentDelimiter = 0xfff3c969
        Operator = 0xff112435
        Number = 0xff112435
        Default = 0xff112435
        Identifier = 0xff112435
        Reference = 0xff112435
        Comment = 0xff112435
        Keyword = 0xff112435
        SyntaxErrorMarker = 0xffff0000
    



