---
layout: archive
title: "Resources for sharing"
permalink: /resources/
author_profile: false
---

<style>
  /* --- 全局容器 --- */
  .resource-container {
    max-width: 1000px;
    margin: 0 auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }


  /* --- 间距工具 --- */
  .section-spacer {
    margin-top: 60px;
    margin-bottom: 40px;
    border-bottom: 1px solid rgba(128, 128, 128, 0.2);
  }

  /* --- 顶部导航 --- */
  .resource-nav {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin: 30px 0;
    padding: 15px;
    background: rgba(128, 128, 128, 0.05);
    border-radius: 50px;
  }

  .resource-nav a {
    text-decoration: none;
    color: #2f7f93;
    font-weight: bold;
    font-size: 1.1em;
    padding: 5px 15px;
    border-radius: 20px;
    transition: all 0.3s;
  }

  .resource-nav a:hover {
    background-color: #2f7f93;
    color: #fff;
    transform: translateY(-2px);
  }

  /* --- 卡片通用样式 --- */
  .resource-card {
    border: 1px solid rgba(128, 128, 128, 0.2);
    border-radius: 10px;
    padding: 25px;
    margin-bottom: 30px;
    background: rgba(128, 128, 128, 0.02);
    transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
  }

  .resource-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    border-color: #2f7f93;
  }

  /* --- 标题样式 --- */
  h2 {
    color: inherit;
    border-bottom: 2px solid rgba(128, 128, 128, 0.2);
    padding-bottom: 10px;
    margin-top: 0;
    margin-bottom: 25px;
    display: inline-block;
    padding-right: 20px;
  }
  
  /* --- 表格样式 --- */
  .table-wrapper {
    overflow-x: auto;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }

  th, td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid rgba(128, 128, 128, 0.2);
  }

  tr:hover {
    background-color: rgba(47, 127, 147, 0.05);
  }
  
  th {
    font-weight: 700;
    color: #2f7f93;
  }

  /* --- 关键修改：徽章区域样式 --- */
  .badges-row, .software-badges {
    margin: 10px 0 20px 0;
    display: flex;
    flex-wrap: wrap; /* 允许换行，防止溢出 */
    align-items: center;
    gap: 6px; /* 紧凑间距，尽量让它们在一行 */
    line-height: 0; /* 消除文字行高影响 */
  }

  /* 让链接变成 flex 盒子，消除底部空白，并防止压缩 */
  .badges-row a, 
  .software-badges a {
    display: flex;
    align-items: center;
    text-decoration: none;
    border-bottom: none !important;
    flex-shrink: 0; /* 禁止被压缩 */
  }

  /* 统一所有徽章高度，禁止压缩 */
  .badges-row img, 
  .software-badges img {
    height: 20px; 
    width: auto;
    display: block;
    flex-shrink: 0; /* 关键：防止徽章变形 */
  }

  /* --- 布局网格 --- */
  .ria-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 20px;
  }
  
  .software-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 25px;
  }

  .small-software-card {
    display: flex;
    flex-direction: column;
    height: 100%;
  }

  .software-img-container {
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 15px 0;
    background: rgba(255,255,255,0.05);
    padding: 10px;
    border-radius: 5px;
  }

  .responsive-img {
    max-width: 100%;
    height: auto;
    border-radius: 4px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }

  .caption {
    display: block; 
    color: #888;
    font-size: 0.9em; 
    font-style: italic; 
    margin-top: auto;
    text-align: center;
  }

  /* --- 协议列表 --- */
  .protocol-list {
    list-style: none;
    padding: 0;
  }

  .protocol-list li {
    padding: 10px 0;
    border-bottom: 1px dashed rgba(128, 128, 128, 0.2);
    display: flex;
    align-items: center;
  }
  
  .protocol-list li::before {
    content: "📄";
    margin-right: 10px;
  }

  /* --- 回到顶部 --- */
  #back-to-top {
    position: fixed;
    bottom: 40px;
    right: 20px;
    padding: 10px 15px;
    font-size: 14px;
    background-color: #2f7f93;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
    z-index: 1000;
    display: none;
  }
  #back-to-top:hover { background-color: #007bff; }
  
  /* 移动端适配 */
  @media (max-width: 768px) {
    .ria-grid {
      grid-template-columns: 1fr;
    }
    .resource-nav {
      flex-wrap: wrap;
      gap: 10px;
    }
  }
</style>

<div class="resource-container">

  <nav class="resource-nav">
    <a href="#plasmids">🧬 Plasmids</a>
    <a href="#software">🖥️ Software</a>
    <a href="#imagej-plugin">
      <img src="/images/resource/imagej/fiji-logo.png" alt="Fiji" style="height: 1.2em; vertical-align: middle; margin-right: 5px;"> 
      ImageJ Plugin
    </a>
    <a href="#protocols">📋 Protocols</a>
  </nav>

  <iframe src="/assets/globe.html" style="width: 90%; max-width: 600px; aspect-ratio: 1 / 1; display: block; margin: 2rem auto; border: none;" scrolling="no"></iframe>


  <div class="section-spacer"></div>
  <h2 id="plasmids">Expression vector maps for biosensors</h2>

  <p>For detailed usage of these biosensors in imaging, or for plasmid related to any other amino acid metabolites requests, please contact <a href="mailto:wangk@ion.ac.cn" style="color: #2f7f93; font-weight: bold;">Dr. Kui Wang</a>.</p>

  <div class="table-wrapper">
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Vector</th>
          <th>Description</th>
          <th>Reference</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><a href="/files/plasmid/K140.dna">K2</a></td>
          <td>pcDNA-GRIT</td>
          <td>Tryptophan sensor expressed in mammalian cell</td>
          <td><a href="/publication/2023-10-31-Tryptophan-sensor">Cell Disc, 2023</a></td>
        </tr>
        <tr>
          <td><a href="/files/plasmid/K140.dna">K3</a></td>
          <td>pcDNA-GRITol</td>
          <td>Tryptophan control sensor expressed in mammalian cell</td>
          <td><a href="/publication/2023-10-31-Tryptophan-sensor">Cell Disc, 2023</a></td>
        </tr>
        <tr>
          <td><a href="/files/plasmid/K140.dna">K4</a></td>
          <td>pcDNA-mito-GRIT</td>
          <td>Mitochondrial Tryptophan sensor expressed in mammalian cell</td>
          <td><a href="/publication/2024-11-14-Tryptophan-imaging">BMC Biol, 2024</a></td>
        </tr>
        <tr>
          <td><a href="/files/plasmid/K140.dna">K5</a></td>
          <td>pcDNA-mito-GRITol</td>
          <td>Mitochondrial Tryptophan control sensor expressed in mammalian cell</td>
          <td><a href="/publication/2024-11-14-Tryptophan-imaging">BMC Biol, 2024</a></td>
        </tr>
        <tr>
          <td><a href="/files/plasmid/PLACEHOLDER.dna">K6</a></td>
          <td>✨GEM<sub>CPPU</sub>1.0 Sensor</td>
          <td>Ratiometric biosensor for detecting Forchlorfenuron (CPPU)</td>
          <td>Manuscript in preparation</td>
        </tr>
        <tr>
          <td><a href="/files/plasmid/PLACEHOLDER.dna">K7</a></td>
          <td>✨GEM<sub>TrpA</sub>1.0 Sensor</td>
          <td>Novel sensor for monitoring Tryptamine dynamics <em>in vivo</em></td>
          <td>Under revision</td>
        </tr>
        <tr id="ado-sensor" >
          <td><a href="/files/plasmid/PLACEHOLDER.dna">K8</a></td>
          <td>✨GEM<sub>Ado</sub>1.0 Sensor</td>
          <td>
              An ultrasensitive, high-contrast sensor for monitoring Adenosine dynamics <em>in vivo</em>. 
              <br><strong>We welcome collaboration to test in diverse model organisms.</strong>
          </td>
          <td>
              <span>Available for <a href="mailto:wangk@ion.ac.cn?subject=Inquiry for Ado Sensor Beta Testing">beta testing</a></span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
More sensors for metabolites are coming...<br><br><br><br>






  <div class="section-spacer"></div>
  <h2 id="software">Ratio Imaging Analyzer (RIA)</h2>

  <div class="resource-card">
    <div style="margin-bottom: 15px;">
      Ratio Imaging Analyzer (RIA) is a lightweight, user-friendly tool designed for processing <strong>dual-channel ratiometric fluorescence data</strong> (e.g., Calcium, FRET, and metabolic sensors). It features automated ratiometric heatmap generation, smart background subtraction, and real-time ROI plotting.
    </div>

  <div class="badges-row">
    <a href="https://pypi.org/project/ria-gui/">
        <img src="https://img.shields.io/pypi/v/ria-gui?color=blue" alt="PyPI">
    </a>
    <a href="https://github.com/Epivitae/RatioImagingAnalyzer/releases/latest">
        <img src="https://img.shields.io/github/v/release/Epivitae/RatioImagingAnalyzer?label=Download&logo=github&color=2ea44f" alt="Download Latest Release">
    </a>

    <img src="https://img.shields.io/badge/python-3.8%2B-yellow" alt="Python Version">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">

    <a href="https://doi.org/10.5281/zenodo.18091693">
        <img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18091693-orange" alt="DOI">
    </a>
    <a href="/#about">
        <img src="https://img.shields.io/badge/Developer-Kui_Wang-2f7f93" alt="Developer">
    </a>

    <a href="https://github.com/Epivitae/RatioImagingAnalyzer">
        <img src="https://img.shields.io/github/stars/Epivitae/RatioImagingAnalyzer?style=social" alt="GitHub stars">
    </a>
  </div>


    <div class="ria-grid">
      <div>
        <div style="font-weight: bold; text-align: center; margin-bottom: 5px;">Automated Workflow</div>
        <img src="/images/resource/analysis.gif" class="responsive-img">
        <span class="caption">Auto-alignment & ratiometric heatmap generation</span>
      </div>
      <div>
        <div style="font-weight: bold; text-align: center; margin-bottom: 5px;">Interactive Analysis</div>
        <img src="/images/resource/live-plot.gif" class="responsive-img">
        <span class="caption">Real-time ROI monitoring & curve plotting</span>
      </div>
    </div>
  </div>


  <h3>🖥️ Other Ready-to-Use Lab Software</h3>
  <br>

  <div class="software-grid">
    
    <div class="resource-card small-software-card">
      <div style="font-size: 1.1em; margin-bottom: 8px;">
        <strong>1. mProcess</strong>
      </div>
      <div style="margin-bottom: 10px; font-size: 0.95em;">
        A self-developed tool for microplate data preprocessing.
      </div>
      
      <div class="software-badges"><a href="https://github.com/Epivitae/mProcess" target="_blank" style="text-decoration: none;"><img src="https://img.shields.io/badge/Source-GitHub-181717?logo=github" alt="GitHub Repo"></a><a href="/files/app/mProcess%20V4.0.exe" style="text-decoration: none;"><img src="https://img.shields.io/badge/Download-mProcess_V4.0-007bff" alt="Download"></a><img src="https://img.shields.io/badge/license-Freeware-green" alt="License"><a href="/#about"><img src="https://img.shields.io/badge/Developer-Kui_Wang-2f7f93" alt="Developer"></a><a href="https://opensource.org/" target="_blank" style="text-decoration: none;"><img src="https://img.shields.io/badge/Open_Source-Yes-2ea44f?logo=open-source-initiative&logoColor=white" alt="Open Source"></a><a href="https://doi.org/10.5281/zenodo.18093335" target="_blank" style="text-decoration: none;"><img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18093335-orange" alt="DOI"></a></div>
      
      <div class="software-img-container">
        <a href="/files/app/pic/mProcess.gif" target="_blank">
          <img src="/files/app/pic/mProcess.gif" alt="mProcess" class="responsive-img">
        </a>
      </div>
      <span class="caption">Batch data processing interface.</span>
    </div>

    <div class="resource-card small-software-card">
      <div style="font-size: 1.1em; margin-bottom: 8px;">
        <strong>2. zGrating</strong>
      </div>
      <div style="margin-bottom: 10px; font-size: 0.95em;">
        A self-developed visual stimulus generator.
      </div>
      
      <div class="software-badges"><a href="/files/app/zGrating_V2.3.exe" style="text-decoration: none;"><img src="https://img.shields.io/badge/Download-zGrating_V2.3-007bff" alt="Download"></a><img src="https://img.shields.io/badge/license-Freeware-green" alt="License"><a href="/#about"><img src="https://img.shields.io/badge/Developer-Kui_Wang-2f7f93" alt="Developer"></a></div>
      
      <div class="software-img-container">
        <a href="/files/app/pic/zGrating.gif" target="_blank">
          <img src="/files/app/pic/zGrating.gif" alt="zGrating" class="responsive-img">
        </a>
      </div>
      <span class="caption">Radial grating pattern generation</span>
    </div>

    <div class="resource-card small-software-card">
      <div style="font-size: 1.1em; margin-bottom: 8px;">
        <strong>3. zStimuli</strong>
      </div>
      <div style="margin-bottom: 10px; font-size: 0.95em;">
        Controls Arduino via serial communication for multimodal stimuli
      </div>
      
      <div class="software-badges"><a href="/files/app/zStimuli4.0.exe" style="text-decoration: none;"><img src="https://img.shields.io/badge/Download-zStimuli_V4.0-007bff" alt="Download"></a><img src="https://img.shields.io/badge/license-Freeware-green" alt="License"><a href="/#about"><img src="https://img.shields.io/badge/Developer-Kui_Wang-2f7f93" alt="Developer"></a></div>
      
      <div class="software-img-container">
        <a href="/files/app/pic/zStimuli.png" target="_blank">
          <img src="/files/app/pic/zStimuli.png" alt="zStimuli" class="responsive-img">
        </a>
      </div>
      <span class="caption">Control panel for experimental stimuli</span>
    </div>

  </div>



  <div class="section-spacer"></div>
  <h2 id="imagej-plugin">
    <img src="/images/resource/imagej/fiji-logo.png" alt="Fiji" style="height: 1.2em; vertical-align: middle; margin-right: 8px;"> 
    ImageJ Plugin
  </h2>

  <div class="resource-card">
      <div style="margin-bottom: 15px;">
        <strong>Biosensor Tools</strong> is a suite of open-source ImageJ/Fiji plugins designed for ratiometric imaging, motion correction, metadata inspection, and AI-powered denoising. As <a href="https://imagej.net/people/Epivitae" target="_blank" style="color: #2f7f93; font-weight: bold; text-decoration: none;">active developers</a> of ImageJ plugins, our team is dedicated to providing biologists with simple and handy analysis tools to facilitate the study of neurochemical dynamics in live animals using genetically encoded fluorescent biosensors.
      </div>

      <div style="background: rgba(47, 127, 147, 0.05); border-left: 4px solid #2f7f93; padding: 15px; border-radius: 4px; margin-bottom: 10px;">
        <strong style="color: #2f7f93;">📥 Quick Installation via Fiji</strong>
        <ol style="margin-top: 8px; margin-bottom: 0; padding-left: 20px; font-size: 0.95em;">
          <li>Open Fiji and navigate to <code>Help > Update...</code></li>
          <li>Click <code>Manage update sites</code>, then click <code>Add update site</code>.</li>
          <li>Enter Name: <strong>Biosensor Tools</strong> and URL: <strong>https://sites.imagej.net/Biosensor-Tools/</strong></li>
          <li>Close the window and click <code>Apply changes</code>.</li>
        </ol>
      </div>
    </div>

    <br>

    <div class="software-grid">
      
    <!-- RIA-J Card -->
    <div class="resource-card small-software-card">
      <div style="font-size: 1.1em; margin-bottom: 8px;">
        <strong>RIA-J</strong> <span style="font-size: 0.85em; color: #666; font-weight: normal;">(Ratio Imaging Analyzer)</span>
      </div>
      <div style="margin-bottom: 10px; font-size: 0.95em;">
        Publication-grade ratiometric analysis. Features background subtraction, pixel-by-pixel ratio calculation, and IMD display mode.
      </div>
      
      <div class="software-badges">
        <a href="https://github.com/Epivitae/RIA-J" target="_blank"><img src="https://img.shields.io/badge/Source-GitHub-181717?logo=github" alt="GitHub Repo"></a>
        <a href="https://imagej.net/plugins/biosensor/ria-j" target="_blank"><img src="https://img.shields.io/badge/ImageJ-Wiki-1565c0" alt="ImageJ Wiki"></a>
      </div>
      
      <div class="software-img-container">
        <a href="https://github.com/Epivitae/RIA-J" target="_blank">
          <img src="/images/resource/imagej/ria-j.png" alt="RIA-J preview" class="responsive-img">
        </a>
      </div>
    </div>

    <!-- FIA Card -->
    <div class="resource-card small-software-card">
      <div style="font-size: 1.1em; margin-bottom: 8px;">
        <strong>FIA</strong> <span style="font-size: 0.85em; color: #666; font-weight: normal;">(Fluorescence Image Aligner)</span>
      </div>
      <div style="margin-bottom: 10px; font-size: 0.95em;">
        Motion correction & Registration. Robustly stabilizes live-animal time-lapse datasets (Global & Dense Flow) before quantification.
      </div>
      
      <div class="software-badges">
        <a href="https://github.com/Epivitae/FIA-Fluorescence-Image-Aligner" target="_blank"><img src="https://img.shields.io/badge/Source-GitHub-181717?logo=github" alt="GitHub Repo"></a>
        <a href="https://imagej.net/plugins/biosensor/fia" target="_blank"><img src="https://img.shields.io/badge/ImageJ-Wiki-1565c0" alt="ImageJ Wiki"></a>
      </div>
      
      <div class="software-img-container">
        <a href="https://github.com/Epivitae/FIA-Fluorescence-Image-Aligner" target="_blank">
          <img src="/images/resource/imagej/compressed-fia-reg.gif" alt="FIA preview" class="responsive-img">
        </a>
      </div>
    </div>

    <!-- MIA Card -->
    <div class="resource-card small-software-card">
      <div style="font-size: 1.1em; margin-bottom: 8px;">
        <strong>MIA</strong> <span style="font-size: 0.85em; color: #666; font-weight: normal;">(Metadata Inspection Analyzer)</span>
      </div>
      <div style="margin-bottom: 10px; font-size: 0.95em;">
        Metadata explorer. Instantly extracts hidden tags (Olympus .oir, OME-XML) and exports summaries to Excel/CSV.
      </div>
      
      <div class="software-badges">
        <a href="https://github.com/Epivitae/MIA-Metadata-Inspection-Analyzer" target="_blank"><img src="https://img.shields.io/badge/Source-GitHub-181717?logo=github" alt="GitHub Repo"></a>
        <a href="https://imagej.net/plugins/biosensor/mia" target="_blank"><img src="https://img.shields.io/badge/ImageJ-Wiki-1565c0" alt="ImageJ Wiki"></a>
      </div>
      
      <div class="software-img-container">
        <a href="https://github.com/Epivitae/MIA-Metadata-Inspection-Analyzer" target="_blank">
          <img src="/images/resource/imagej/mia-gui.png" alt="MIA preview" class="responsive-img">
        </a>
      </div>
    </div>

    <!-- NIA Card -->
    <div class="resource-card small-software-card">
      <div style="font-size: 1.1em; margin-bottom: 8px;">
        <strong>NIA</strong> <span style="font-size: 0.85em; color: #666; font-weight: normal;">(Neural Inference Assistant)</span>
      </div>
      <div style="margin-bottom: 10px; font-size: 0.95em;">
        Zero-setup AI denoising. Runs deep learning models (DnCNN) directly in Java via ONNX Runtime. No Python/CUDA required. Supports 5D hyperstacks.
      </div>
      
      <div class="software-badges">
        <a href="https://github.com/Epivitae/NIA-Denoise" target="_blank"><img src="https://img.shields.io/badge/Source-GitHub-181717?logo=github" alt="GitHub Repo"></a>
        <a href="https://imagej.net/plugins/biosensor/nia" target="_blank"><img src="https://img.shields.io/badge/ImageJ-Wiki-1565c0" alt="ImageJ Wiki"></a>
      </div>
      
      <div class="software-img-container">
        <a href="https://github.com/Epivitae/NIA-Denoise" target="_blank">
          <img src="https://opengraph.githubassets.com/1/Epivitae/NIA-Denoise" alt="NIA preview" class="responsive-img">
        </a>
      </div>
    </div>

    <!-- WinMan Card -->
    <div class="resource-card small-software-card">
      <div style="font-size: 1.1em; margin-bottom: 8px;">
        <strong>WinMan</strong> <span style="font-size: 0.85em; color: #666; font-weight: normal;">(Window Manager)</span>
      </div>
      <div style="margin-bottom: 10px; font-size: 0.95em;">
        Workspace accelerator. Efficiently manages, tiles, and filters multiple image windows to keep your ImageJ workspace clean.
      </div>
      
      <div class="software-badges">
        <a href="https://github.com/Epivitae/WinMan" target="_blank"><img src="https://img.shields.io/badge/Source-GitHub-181717?logo=github" alt="GitHub Repo"></a>
        <a href="https://imagej.net/plugins/biosensor/winman" target="_blank"><img src="https://img.shields.io/badge/ImageJ-Wiki-1565c0" alt="ImageJ Wiki"></a>
      </div>
      
      <div class="software-img-container">
        <a href="https://github.com/Epivitae/WinMan" target="_blank">
          <img src="https://opengraph.githubassets.com/1/Epivitae/WinMan" alt="WinMan preview" class="responsive-img">
        </a>
      </div>
    </div>



    </div>


  <div class="section-spacer"></div>
  <h2 id="protocols">Protocols in our hands</h2>

  <div class="resource-card">
    <ul class="protocol-list">
      <li>
        <a href="/files/protocol/K.WANG Molecular cloning Methods in our hands (V1.0).pdf">High-throughput recombinant DNA preparation</a>
      </li>
      <li>
        <a href="/files/protocol/K.WANG%20Tol2%20mRNA%20IVT%20protocol.pdf"><em>In vitro</em> transcription for mRNA preparation</a>
      </li>
      <li>
        Biosensor protein purification
      </li>
      <li>
        Fluorescent biosensor screening and modification
      </li>
    </ul>
  </div>

  <div class="section-spacer"></div>
  <h3>Useful codes</h3>
  <pre style="background: rgba(128,128,128,0.1); padding: 10px; border-radius: 5px;">bundle exec jekyll serve --livereload --incremental

jekyll clean</pre>

</div>

<button id="back-to-top" onclick="scrollToTop()">⬆️ Back to Top</button>

<script>
  var mybutton = document.getElementById("back-to-top");
  window.onscroll = function() {scrollFunction()};
  function scrollFunction() {
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }
  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
</script>