<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
    <head>
      <style>
        svg {
          border: 1px solid black;
        }
      </style>
    </head>
    <body>
      <svg width="{dibuix/canvas/amplada}" height="{dibuix/canvas/alçada}" xmlns="http://www.w3.org/2000/svg">
        <xsl:for-each select="dibuix/figures/figura">

          <xsl:choose>
            <xsl:when test="@tipus = 'rectangle'">
              <rect x="{posicio/x}" y="{posicio/y}" width="{dimensions/amplada}" height="{dimensions/alçada}" fill="{@color}" />
            </xsl:when>
            <xsl:when test="@tipus = 'cercle'">
              <circle cx="{centre/x}" cy="{centre/y}" r="{radi}" fill="{@color}" />
            </xsl:when>
            <xsl:when test="@tipus = 'ellipse'">
              <ellipse cx="{centre/x}" cy="{centre/y}" rx="{radi_x}" ry="{radi_y}" fill="{@color}" />
            </xsl:when>
            <xsl:otherwise>
              <text x="0" y="15" fill="red">Tipus erroni: <xsl:value-of select="@tipus"/> </text>
            </xsl:otherwise>
          </xsl:choose>

        </xsl:for-each>
      </svg>
    </body>
  </html>
</xsl:template>

</xsl:stylesheet>