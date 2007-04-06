<?xml version="1.0" encoding="ISO-8859-1" ?> 
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
  	<xsl:apply-templates select="info" /> 
  </xsl:template>
  <xsl:template match="infowindow">
  	
	<table width="215" cellspacing="15">
	<tr>
	<td style="font-size:14pt;text-align:Left;" colspan="2">
		<xsl:value-of select="title" /> 
	</td>
	</tr>
	<tr valign="top">
	<td style="font-size:12pt;font-weight:bold;text-align:Left;">
		Address
	</td>
	<td style="font-size:12pt;text-align:Left;">
		<xsl:value-of select="address" /> <br/>
		<xsl:value-of select="city" /> <br/>
		<xsl:value-of select="postcode" /> <br/>
	</td>
	</tr>
	<tr>
	<td style="font-size:12pt;font-weight:bold;text-align:Left;">
		Phone
	</td>
	<td style="font-size:12pt;text-align:Left;">
		<xsl:value-of select="phone" /> 
	</td>
	</tr>
</table>
</xsl:template>
</xsl:stylesheet>