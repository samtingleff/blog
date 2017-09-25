<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0"
     xmlns:atom="http://www.w3.org/2005/Atom">
 <channel>
  <atom:link href="http://sam.tingleff.com/feed.rss" rel="self" type="application/rss+xml" />
  <title>marginal focus</title>
  <description>marginal focus | Sam Tingleff</description>
  <link>http://sam.tingleff.com/</link>
  <copyright>Copyright 2017 Sam Tingleff</copyright>
  <language>en-us</language>
  <lastBuildDate>$buildDate$</lastBuildDate>
  <pubDate>$buildDate$</pubDate>
  <generator>https://github.com/samtingleff/yassg</generator>
  $items:{item|
   <item>
    <title>$item.title$</title>
    <description><![CDATA[$item.body$]]></description>
    <guid isPermaLink="true">http://sam.tingleff.com/$item.href$</guid>
    <link>http://sam.tingleff.com/$item.href$</link>
    $item.tags:{tag|
     <category>$tag$</category>
    }$
    <comments>http://sam.tingleff.com/$item.href$</comments>
    <pubDate>$item.pubDateRSS$</pubDate>
   </item>
  }$
 </channel>
</rss>
