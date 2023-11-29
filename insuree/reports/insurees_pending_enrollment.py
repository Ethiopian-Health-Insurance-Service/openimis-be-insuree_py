from django.conf import settings
from django.db import connection

from tools.utils import dictfetchall
import logging
logger = logging.getLogger(__name__)

# If manually pasting from ReportBro and you have test data, search and replace \" with \\"
template = """
{
  "docElements": [
    {
      "elementType": "text",
      "id": 3,
      "containerId": "0_header",
      "x": 0,
      "y": 20,
      "width": 575,
      "height": 40,
      "content": "Insurees pending enrollment",
      "richText": false,
      "richTextContent": null,
      "richTextHtml": "",
      "eval": false,
      "styleId": "",
      "bold": true,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "center",
      "verticalAlignment": "middle",
      "textColor": "#6aa84f",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": "24",
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": 1,
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": 2,
      "paddingTop": 2,
      "paddingRight": 2,
      "paddingBottom": 2,
      "printIf": "",
      "removeEmptyElement": false,
      "alwaysPrintOnSamePage": true,
      "pattern": "",
      "link": "",
      "cs_condition": "",
      "cs_styleId": "",
      "cs_bold": false,
      "cs_italic": false,
      "cs_underline": false,
      "cs_strikethrough": false,
      "cs_horizontalAlignment": "left",
      "cs_verticalAlignment": "top",
      "cs_textColor": "#000000",
      "cs_backgroundColor": "",
      "cs_font": "helvetica",
      "cs_fontSize": 12,
      "cs_lineSpacing": 1,
      "cs_borderColor": "#000000",
      "cs_borderWidth": "1",
      "cs_borderAll": false,
      "cs_borderLeft": false,
      "cs_borderTop": false,
      "cs_borderRight": false,
      "cs_borderBottom": false,
      "cs_paddingLeft": 2,
      "cs_paddingTop": 2,
      "cs_paddingRight": 2,
      "cs_paddingBottom": 2,
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_colspan": "",
      "spreadsheet_addEmptyRow": false,
      "spreadsheet_textWrap": false
    },
    {
      "elementType": "line",
      "id": 158,
      "containerId": "0_content",
      "x": 0,
      "y": 0,
      "width": 575,
      "height": 1,
      "color": "#000000",
      "printIf": ""
    },
    {
      "elementType": "text",
      "id": 193,
      "containerId": "0_content",
      "x": 0,
      "y": 10,
      "width": 575,
      "height": 20,
      "content": "From ${StartDate} to ${EndDate}",
      "richText": false,
      "richTextContent": null,
      "richTextHtml": "",
      "eval": false,
      "styleId": "",
      "bold": true,
      "italic": false,
      "underline": true,
      "strikethrough": false,
      "horizontalAlignment": "left",
      "verticalAlignment": "top",
      "textColor": "#000000",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": 12,
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": 1,
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": 2,
      "paddingTop": 2,
      "paddingRight": 2,
      "paddingBottom": 2,
      "printIf": "",
      "removeEmptyElement": false,
      "alwaysPrintOnSamePage": true,
      "pattern": "",
      "link": "",
      "cs_condition": "",
      "cs_styleId": "",
      "cs_bold": false,
      "cs_italic": false,
      "cs_underline": false,
      "cs_strikethrough": false,
      "cs_horizontalAlignment": "left",
      "cs_verticalAlignment": "top",
      "cs_textColor": "#000000",
      "cs_backgroundColor": "",
      "cs_font": "helvetica",
      "cs_fontSize": 12,
      "cs_lineSpacing": 1,
      "cs_borderColor": "#000000",
      "cs_borderWidth": "1",
      "cs_borderAll": false,
      "cs_borderLeft": false,
      "cs_borderTop": false,
      "cs_borderRight": false,
      "cs_borderBottom": false,
      "cs_paddingLeft": 2,
      "cs_paddingTop": 2,
      "cs_paddingRight": 2,
      "cs_paddingBottom": 2,
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_colspan": "",
      "spreadsheet_addEmptyRow": false,
      "spreadsheet_textWrap": false
    },
    {
      "elementType": "table",
      "id": 195,
      "containerId": "0_content",
      "width": 574,
      "x": 0,
      "y": 40,
      "dataSource": "${data}",
      "columns": 4,
      "header": true,
      "contentRows": 1,
      "footer": false,
      "border": "grid",
      "borderColor": "#000000",
      "borderWidth": "1",
      "printIf": "",
      "removeEmptyElement": false,
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_addEmptyRow": false,
      "headerData": {
        "elementType": "none",
        "id": 196,
        "height": 20,
        "backgroundColor": "",
        "repeatHeader": true,
        "columnData": [
          {
            "elementType": "table_text",
            "id": 197,
            "width": 160,
            "content": "Insurance Nb",
            "eval": false,
            "colspan": "",
            "styleId": "33",
            "bold": true,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "middle",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": "12",
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "printIf": "",
            "growWeight": 0,
            "borderWidth": 1
          },
          {
            "elementType": "table_text",
            "id": 205,
            "width": 175,
            "content": "Name",
            "eval": false,
            "colspan": "",
            "styleId": "33",
            "bold": true,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "middle",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": "12",
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "printIf": "",
            "growWeight": 0,
            "borderWidth": 1
          },
          {
            "elementType": "table_text",
            "id": 206,
            "width": 168,
            "content": "Photo Date",
            "eval": false,
            "colspan": "",
            "styleId": "33",
            "bold": true,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "middle",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": "12",
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "printIf": "",
            "growWeight": 0,
            "borderWidth": 1
          },
          {
            "elementType": "table_text",
            "id": 239,
            "width": 71,
            "content": "Duplicated",
            "eval": false,
            "colspan": "",
            "styleId": "33",
            "bold": true,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "middle",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": "12",
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "printIf": "",
            "growWeight": 0,
            "borderWidth": 1
          }
        ]
      },
      "contentDataRows": [
        {
          "elementType": "none",
          "id": 199,
          "height": 20,
          "backgroundColor": "",
          "alternateBackgroundColor": "#eeeeee",
          "groupExpression": "",
          "printIf": "",
          "alwaysPrintOnSamePage": false,
          "pageBreak": false,
          "repeatGroupHeader": false,
          "columnData": [
            {
              "elementType": "table_text",
              "id": 200,
              "width": 160,
              "content": "${CHFID}",
              "eval": false,
              "colspan": "",
              "styleId": "",
              "bold": false,
              "italic": false,
              "underline": false,
              "strikethrough": false,
              "horizontalAlignment": "left",
              "verticalAlignment": "top",
              "textColor": "#000000",
              "backgroundColor": "",
              "font": "helvetica",
              "fontSize": 12,
              "lineSpacing": 1,
              "paddingLeft": 2,
              "paddingTop": 2,
              "paddingRight": 2,
              "paddingBottom": 2,
              "pattern": "",
              "link": "",
              "cs_condition": "",
              "cs_styleId": "",
              "cs_bold": false,
              "cs_italic": false,
              "cs_underline": false,
              "cs_strikethrough": false,
              "cs_horizontalAlignment": "left",
              "cs_verticalAlignment": "top",
              "cs_textColor": "#000000",
              "cs_backgroundColor": "",
              "cs_font": "helvetica",
              "cs_fontSize": 12,
              "cs_lineSpacing": 1,
              "cs_paddingLeft": 2,
              "cs_paddingTop": 2,
              "cs_paddingRight": 2,
              "cs_paddingBottom": 2,
              "spreadsheet_textWrap": false,
              "borderWidth": 1,
              "growWeight": 0
            },
            {
              "elementType": "table_text",
              "id": 208,
              "width": 175,
              "content": "${OtherNames} + ' ' + ${LastName}",
              "eval": true,
              "colspan": "",
              "styleId": "",
              "bold": false,
              "italic": false,
              "underline": false,
              "strikethrough": false,
              "horizontalAlignment": "left",
              "verticalAlignment": "top",
              "textColor": "#000000",
              "backgroundColor": "",
              "font": "helvetica",
              "fontSize": 12,
              "lineSpacing": 1,
              "paddingLeft": 2,
              "paddingTop": 2,
              "paddingRight": 2,
              "paddingBottom": 2,
              "pattern": "",
              "link": "",
              "cs_condition": "",
              "cs_styleId": "",
              "cs_bold": false,
              "cs_italic": false,
              "cs_underline": false,
              "cs_strikethrough": false,
              "cs_horizontalAlignment": "left",
              "cs_verticalAlignment": "top",
              "cs_textColor": "#000000",
              "cs_backgroundColor": "",
              "cs_font": "helvetica",
              "cs_fontSize": 12,
              "cs_lineSpacing": 1,
              "cs_paddingLeft": 2,
              "cs_paddingTop": 2,
              "cs_paddingRight": 2,
              "cs_paddingBottom": 2,
              "spreadsheet_textWrap": false,
              "borderWidth": 1,
              "growWeight": 0
            },
            {
              "elementType": "table_text",
              "id": 209,
              "width": 168,
              "content": "${photodate}",
              "eval": false,
              "colspan": "",
              "styleId": "",
              "bold": false,
              "italic": false,
              "underline": false,
              "strikethrough": false,
              "horizontalAlignment": "left",
              "verticalAlignment": "top",
              "textColor": "#000000",
              "backgroundColor": "",
              "font": "helvetica",
              "fontSize": 12,
              "lineSpacing": 1,
              "paddingLeft": 2,
              "paddingTop": 2,
              "paddingRight": 2,
              "paddingBottom": 2,
              "pattern": "yyyy/MM/dd",
              "link": "",
              "cs_condition": "",
              "cs_styleId": "",
              "cs_bold": false,
              "cs_italic": false,
              "cs_underline": false,
              "cs_strikethrough": false,
              "cs_horizontalAlignment": "left",
              "cs_verticalAlignment": "top",
              "cs_textColor": "#000000",
              "cs_backgroundColor": "",
              "cs_font": "helvetica",
              "cs_fontSize": 12,
              "cs_lineSpacing": 1,
              "cs_paddingLeft": 2,
              "cs_paddingTop": 2,
              "cs_paddingRight": 2,
              "cs_paddingBottom": 2,
              "spreadsheet_textWrap": false,
              "borderWidth": 1,
              "growWeight": 0
            },
            {
              "elementType": "table_text",
              "id": 240,
              "width": 71,
              "content": "${duplicated}",
              "eval": false,
              "colspan": "",
              "styleId": "",
              "bold": false,
              "italic": false,
              "underline": false,
              "strikethrough": false,
              "horizontalAlignment": "left",
              "verticalAlignment": "top",
              "textColor": "#000000",
              "backgroundColor": "",
              "font": "helvetica",
              "fontSize": 12,
              "lineSpacing": 1,
              "paddingLeft": 2,
              "paddingTop": 2,
              "paddingRight": 2,
              "paddingBottom": 2,
              "pattern": "",
              "link": "",
              "cs_condition": "",
              "cs_styleId": "",
              "cs_bold": false,
              "cs_italic": false,
              "cs_underline": false,
              "cs_strikethrough": false,
              "cs_horizontalAlignment": "left",
              "cs_verticalAlignment": "top",
              "cs_textColor": "#000000",
              "cs_backgroundColor": "",
              "cs_font": "helvetica",
              "cs_fontSize": 12,
              "cs_lineSpacing": 1,
              "cs_paddingLeft": 2,
              "cs_paddingTop": 2,
              "cs_paddingRight": 2,
              "cs_paddingBottom": 2,
              "spreadsheet_textWrap": false,
              "borderWidth": 1,
              "growWeight": 0
            }
          ]
        }
      ],
      "footerData": {
        "elementType": "none",
        "id": 202,
        "height": 20,
        "backgroundColor": "",
        "columnData": [
          {
            "elementType": "table_text",
            "id": 203,
            "width": 160,
            "content": "",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": false,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "top",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "borderWidth": 1,
            "growWeight": 0
          },
          {
            "elementType": "table_text",
            "id": 211,
            "width": 175,
            "content": "",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": false,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "top",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "borderWidth": 1,
            "growWeight": 0
          },
          {
            "elementType": "table_text",
            "id": 212,
            "width": 168,
            "content": "",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": false,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "top",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "borderWidth": 1,
            "growWeight": 0
          },
          {
            "elementType": "table_text",
            "id": 241,
            "width": 71,
            "content": "",
            "eval": false,
            "colspan": "",
            "styleId": "",
            "bold": false,
            "italic": false,
            "underline": false,
            "strikethrough": false,
            "horizontalAlignment": "left",
            "verticalAlignment": "top",
            "textColor": "#000000",
            "backgroundColor": "",
            "font": "helvetica",
            "fontSize": 12,
            "lineSpacing": 1,
            "paddingLeft": 2,
            "paddingTop": 2,
            "paddingRight": 2,
            "paddingBottom": 2,
            "pattern": "",
            "link": "",
            "cs_condition": "",
            "cs_styleId": "",
            "cs_bold": false,
            "cs_italic": false,
            "cs_underline": false,
            "cs_strikethrough": false,
            "cs_horizontalAlignment": "left",
            "cs_verticalAlignment": "top",
            "cs_textColor": "#000000",
            "cs_backgroundColor": "",
            "cs_font": "helvetica",
            "cs_fontSize": 12,
            "cs_lineSpacing": 1,
            "cs_paddingLeft": 2,
            "cs_paddingTop": 2,
            "cs_paddingRight": 2,
            "cs_paddingBottom": 2,
            "spreadsheet_textWrap": false,
            "borderWidth": 1,
            "growWeight": 0
          }
        ]
      }
    },
    {
      "elementType": "text",
      "id": 7,
      "containerId": "0_footer",
      "x": 320,
      "y": 0,
      "width": 255,
      "height": 30,
      "content": "Page ${page_number} / ${page_count}",
      "richText": false,
      "richTextContent": null,
      "richTextHtml": "",
      "eval": false,
      "styleId": "",
      "bold": false,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "right",
      "verticalAlignment": "middle",
      "textColor": "#666666",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": 12,
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": 1,
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": 2,
      "paddingTop": 2,
      "paddingRight": 2,
      "paddingBottom": 2,
      "printIf": "",
      "removeEmptyElement": false,
      "alwaysPrintOnSamePage": true,
      "pattern": "",
      "link": "",
      "cs_condition": "",
      "cs_styleId": "",
      "cs_bold": false,
      "cs_italic": false,
      "cs_underline": false,
      "cs_strikethrough": false,
      "cs_horizontalAlignment": "left",
      "cs_verticalAlignment": "top",
      "cs_textColor": "#000000",
      "cs_backgroundColor": "",
      "cs_font": "helvetica",
      "cs_fontSize": 12,
      "cs_lineSpacing": 1,
      "cs_borderColor": "#000000",
      "cs_borderWidth": "1",
      "cs_borderAll": false,
      "cs_borderLeft": false,
      "cs_borderTop": false,
      "cs_borderRight": false,
      "cs_borderBottom": false,
      "cs_paddingLeft": 2,
      "cs_paddingTop": 2,
      "cs_paddingRight": 2,
      "cs_paddingBottom": 2,
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_colspan": "",
      "spreadsheet_addEmptyRow": false,
      "spreadsheet_textWrap": false
    },
    {
      "elementType": "text",
      "id": 8,
      "containerId": "0_footer",
      "x": 0,
      "y": 0,
      "width": 290,
      "height": 30,
      "content": "Created on ${current_date}",
      "richText": false,
      "richTextContent": null,
      "richTextHtml": "",
      "eval": false,
      "styleId": "",
      "bold": false,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "left",
      "verticalAlignment": "middle",
      "textColor": "#666666",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": 12,
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": 1,
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": 2,
      "paddingTop": 2,
      "paddingRight": 2,
      "paddingBottom": 2,
      "printIf": "",
      "removeEmptyElement": false,
      "alwaysPrintOnSamePage": true,
      "pattern": "",
      "link": "",
      "cs_condition": "",
      "cs_styleId": "",
      "cs_bold": false,
      "cs_italic": false,
      "cs_underline": false,
      "cs_strikethrough": false,
      "cs_horizontalAlignment": "left",
      "cs_verticalAlignment": "top",
      "cs_textColor": "#000000",
      "cs_backgroundColor": "",
      "cs_font": "helvetica",
      "cs_fontSize": 12,
      "cs_lineSpacing": 1,
      "cs_borderColor": "#000000",
      "cs_borderWidth": "1",
      "cs_borderAll": false,
      "cs_borderLeft": false,
      "cs_borderTop": false,
      "cs_borderRight": false,
      "cs_borderBottom": false,
      "cs_paddingLeft": 2,
      "cs_paddingTop": 2,
      "cs_paddingRight": 2,
      "cs_paddingBottom": 2,
      "spreadsheet_hide": false,
      "spreadsheet_column": "",
      "spreadsheet_colspan": "",
      "spreadsheet_addEmptyRow": false,
      "spreadsheet_textWrap": false
    }
  ],
  "parameters": [
    {
      "id": 1,
      "name": "page_count",
      "type": "number",
      "arrayItemType": "string",
      "eval": false,
      "nullable": false,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": true,
      "testData": ""
    },
    {
      "id": 2,
      "name": "page_number",
      "type": "number",
      "arrayItemType": "string",
      "eval": false,
      "nullable": false,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": true,
      "testData": ""
    },
    {
      "id": 9,
      "name": "current_date",
      "type": "date",
      "arrayItemType": "string",
      "eval": false,
      "nullable": false,
      "pattern": "d/M/yyyy H:mm",
      "expression": "",
      "showOnlyNameType": false,
      "testData": ""
    },
    {
      "id": 233,
      "name": "data",
      "type": "array",
      "arrayItemType": "string",
      "eval": false,
      "nullable": false,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": false,
      "testData": "",
      "children": [
        {
          "id": 234,
          "name": "row_number",
          "type": "number",
          "arrayItemType": "string",
          "eval": false,
          "nullable": false,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": true,
          "testData": ""
        },
        {
          "id": 235,
          "name": "OfficerID",
          "type": "number",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 236,
          "name": "Code",
          "type": "string",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 262,
          "name": "OtherNames",
          "type": "string",
          "arrayItemType": "string",
          "eval": false,
          "nullable": false,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 237,
          "name": "LastName",
          "type": "string",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 242,
          "name": "CHFID",
          "type": "string",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 244,
          "name": "photodate",
          "type": "date",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 250,
          "name": "duplicated",
          "type": "string",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 251,
          "name": "rno",
          "type": "number",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        },
        {
          "id": 263,
          "name": "OfficerStatus",
          "type": "string",
          "arrayItemType": "string",
          "eval": false,
          "nullable": true,
          "pattern": "",
          "expression": "",
          "showOnlyNameType": false,
          "testData": ""
        }
      ]
    },
    {
      "id": 264,
      "name": "StartDate",
      "type": "string",
      "arrayItemType": "string",
      "eval": false,
      "nullable": true,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": false,
      "testData": ""
    },
    {
      "id": 265,
      "name": "EndDate",
      "type": "string",
      "arrayItemType": "string",
      "eval": false,
      "nullable": true,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": false,
      "testData": ""
    },
    {
      "id": 266,
      "name": "OfficerCode",
      "type": "string",
      "arrayItemType": "string",
      "eval": false,
      "nullable": true,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": false,
      "testData": ""
    },
    {
      "id": 267,
      "name": "OfficerName",
      "type": "string",
      "arrayItemType": "string",
      "eval": false,
      "nullable": true,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": false,
      "testData": ""
    },
    {
      "id": 268,
      "name": "LocationName",
      "type": "string",
      "arrayItemType": "string",
      "eval": false,
      "nullable": true,
      "pattern": "",
      "expression": "",
      "showOnlyNameType": false,
      "testData": ""
    }
  ],
  "styles": [
    {
      "id": 33,
      "name": "Table Header",
      "bold": true,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "left",
      "verticalAlignment": "middle",
      "textColor": "#000000",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": "12",
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": "1",
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": "2",
      "paddingTop": "2",
      "paddingRight": "2",
      "paddingBottom": "2"
    },
    {
      "id": 34,
      "name": "Table Content",
      "bold": false,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "left",
      "verticalAlignment": "middle",
      "textColor": "#000000",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": "9",
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": "1",
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": "2",
      "paddingTop": "2",
      "paddingRight": "2",
      "paddingBottom": "2"
    },
    {
      "id": 35,
      "name": "Table Content Highlight",
      "bold": true,
      "italic": false,
      "underline": false,
      "strikethrough": false,
      "horizontalAlignment": "center",
      "verticalAlignment": "middle",
      "textColor": "#3d85c6",
      "backgroundColor": "",
      "font": "helvetica",
      "fontSize": "9",
      "lineSpacing": 1,
      "borderColor": "#000000",
      "borderWidth": "1",
      "borderAll": false,
      "borderLeft": false,
      "borderTop": false,
      "borderRight": false,
      "borderBottom": false,
      "paddingLeft": "2",
      "paddingTop": "2",
      "paddingRight": "2",
      "paddingBottom": "2"
    }
  ],
  "version": 3,
  "documentProperties": {
    "pageFormat": "A4",
    "pageWidth": "",
    "pageHeight": "",
    "unit": "mm",
    "orientation": "portrait",
    "contentHeight": "",
    "marginLeft": "10",
    "marginTop": "10",
    "marginRight": "10",
    "marginBottom": "10",
    "header": true,
    "headerSize": "80",
    "headerDisplay": "always",
    "footer": true,
    "footerSize": "30",
    "footerDisplay": "always",
    "patternLocale": "en",
    "patternCurrencySymbol": "$"
  }
}
"""


insurees_pending_enrollment = f"""
WITH PendingInsurees AS
         (SELECT O."OfficerID",
                 O."Code",
                 O."OtherNames",
                 O."LastName",
                 P."CHFID",
                 MAX(P."PhotoDate")                                                  PhotoDate,
                 ROW_NUMBER() OVER (PARTITION BY P."CHFID" ORDER BY O."OfficerID")   RNo,
                 case 
                    when CAST(O."WorksTo" AS DATE) <= CAST({'GETDATE()' if settings.MSSQL else 'NOW()'} AS DATE) 
                    THEN 'N' 
                    ELSE 'A'
                 END OfficerStatus
          FROM "tblSubmittedPhotos" P
                   LEFT OUTER JOIN "tblInsuree" I ON P."CHFID" = I."CHFID"
                   INNER JOIN "tblOfficer" O ON P."OfficerCode" = O."Code"
                   INNER JOIN "tblDistricts" L ON L."DistrictId" = O."LocationId" OR L."Region" = O."LocationId"
          WHERE I."ValidityTo" Is NULL
            AND I."InsureeID" IS NULL  -- Insuree not enrolled
            AND O."ValidityTo" IS NULL
            AND (L."Region" = %(LocationId)s OR L."DistrictId" = %(LocationId)s OR %(LocationId)s = 0)
            AND (O."OfficerID" = %(OfficerId)s OR %(OfficerId)s = 0)
            AND P."PhotoDate" BETWEEN %(StartDate)s AND %(EndDate)s
          GROUP BY O."OfficerID", O."Code", O."OtherNames", O."LastName", P."CHFID", O."WorksTo")
SELECT "OfficerID",
       "Code",
       "OtherNames",
       "LastName",
       "CHFID",
       PhotoDate,
       case when RNo = 1 then '' else 'Duplicated' END Duplicated,
       CASE WHEN RNo = 1 THEN 1 ELSE 0 END RNo,
       OfficerStatus
FROM PendingInsurees
"""


def insurees_pending_enrollment_query(user, officerId=0, locationId=0, dateFrom=None, dateTo=None, **kwargs):
    with connection.cursor() as cur:
        try:
            cur.execute(
                insurees_pending_enrollment,
                {
                    "OfficerId": officerId,
                    "LocationId": locationId,
                    "StartDate": dateFrom,
                    "EndDate": dateTo,
                },
            )
            return {
                "StartDate": dateFrom,
                "EndDate": dateTo,
                "data": dictfetchall(cur)
            }
        except Exception as e:
            logger.exception("Error fetching missing photo query")
            raise e

    logger.error("Pending enrollment query arrived at end of function")
    return {"data": None}
