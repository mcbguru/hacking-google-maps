<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/">
        <xsl:apply-templates select="rsp" />
    </xsl:template>
    <xsl:template match="photo">
        
        <table width="230" cellspacing="15">
            <tr>
                <td style="font-size:10pt;font-weight:bold;text-align:Left;">
                    Title
                </td>
                <td style="font-size:10pt;text-align:Left;" colspan="2">
                    <xsl:value-of select="title" />
                </td>
            </tr>
            <tr>
                <td style="font-size:10pt;font-weight:bold;text-align:Left;">
                    Description
                </td>
                <td style="font-size:10pt;text-align:Left;" colspan="2">
                    <xsl:value-of select="description" />
                </td>
            </tr>
            <tr>
                <td style="font-size:10pt;font-weight:bold;text-align:Left;">
                    Taken
                </td>
                <td style="font-size:10pt;text-align:Left;" colspan="2">
                    <xsl:value-of select="dates/@taken" />
                </td>
            </tr>
            <tr valign="top">
                <td style="font-size:10pt;font-weight:bold;text-align:Left;">
                    Image
                </td>
                <td style="font-size:10pt;text-align:Left;">
                    <a>
                        <xsl:attribute name="href">
                            <xsl:value-of select="urls/url" />
                        </xsl:attribute>
                      <img>
                        <xsl:attribute name="src">http://static.flickr.com/<xsl:value-of select="@server" />/<xsl:value-of select="@id" />_<xsl:value-of select="@secret" />_s.jpg</xsl:attribute>
                      </img>
                        </a>
                </td>
            </tr>
        </table>

    </xsl:template>
</xsl:stylesheet>
