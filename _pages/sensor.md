---
layout: archive
title: ""
permalink: /sensor/
author_profile: false
---

<style>
/* 1. 基础容器设置 */
.embed-container {
    position: relative;
    height: 100vh; /* 保持一屏高度 */
    overflow: hidden;
    background: #fff; /* 防止加载时背景透明 */
    border-radius: 8px; /* 加一点圆角，更精致 */
    box-shadow: 0 4px 12px rgba(0,0,0,0.1); /* 加一点阴影，让它浮起来 */
}

.embed-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0;
}

/* 2. 居中与宽度控制 */
.wide-wrapper {
    position: relative;
    
    /* 核心修改：宽度设为 90%，不要 100% */
    width: 90vw; 
    
    /* 核心修改：设置上限，防止在超宽屏上太难看 */
    max-width: 1400px; 
    
    /* 现代 CSS 居中大法：向左走 50%，再回退自身的一半 */
    left: 50%;
    transform: translateX(-50%);
}
</style>

<div class="wide-wrapper">
    <div class="embed-container">
        <iframe 
            src="https://sensor.cns.ac.cn" 
            frameborder="0" 
            allowfullscreen>
        </iframe>
    </div>
</div>

<div style="text-align: center; margin-top: 20px; font-size: 0.9em; color: #666;">
    _Data is automatically updated daily. If the database fails to load, <a href="https://autosensorbase.streamlit.app" target="_blank">click here</a> to open in a new tab._
</div>