---
permalink: /
title: ""
redirect_from:
  - /about/
  - /about.html
  - /news/
comments: true
---

<style>
  /* --- 全局容器 --- */
  .page-container {
    max-width: 900px;
    margin: 0 auto;
    /* 关键：不设定 color 和 background，直接继承主题的 body 设置 */
  }

  /* --- 标题通用样式 --- */
  .section-heading {
    font-size: 2em;
    font-weight: 700;
    margin-top: 60px;
    margin-bottom: 30px;
    padding-bottom: 15px;
    /* 使用半透明边框，无论黑底白底都能看到一条淡淡的线 */
    border-bottom: 2px solid rgba(128, 128, 128, 0.2); 
    position: relative;
    color: inherit; /* 继承主题标题颜色 */
  }
  
  /* 标题下的蓝色装饰线 (保留品牌色) */
  .section-heading::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 60px;
    height: 2px;
    background-color: #2f7f93; 
  }

  /* --- About 部分样式 --- */
  .about-content {
    font-size: 1.1em;
    line-height: 1.8;
    text-align: justify;
    color: inherit; /* 关键：继承主题默认文字颜色 */
  }

  .about-content p {
    margin-bottom: 20px;
  }

  /* 链接样式：保留品牌色，但悬停效果适配 */
  .about-content a, .news-body a {
    color: #2f7f93; /* 品牌蓝在深色/浅色背景下通常都可见 */
    text-decoration: none;
    font-weight: 500;
    border-bottom: 1px dotted #2f7f93;
    transition: all 0.2s;
  }

  .about-content a:hover, .news-body a:hover {
    opacity: 0.7; /* 悬停时不改颜色，而是改透明度，这样更兼容 */
    border-bottom-style: solid;
  }

  /* --- News 时间轴样式 --- */
  .news-feed {
    display: flex;
    flex-direction: column;
    gap: 30px;
  }

  .news-item {
    display: flex;
    gap: 25px;
    padding-bottom: 25px;
    /* 使用半透明边框作为分割线 */
    border-bottom: 1px solid rgba(128, 128, 128, 0.2); 
  }

  .news-item:last-child {
    border-bottom: none;
  }

  /* 日期列 */
  .news-date {
    flex-shrink: 0;
    width: 120px;
    font-family: "Courier New", Courier, monospace;
    font-weight: bold;
    color: #2f7f93; /* 日期使用品牌色，突出显示 */
    font-size: 0.95em;
    text-align: right;
    padding-top: 2px;
  }

  /* 内容列 */
  .news-body {
    flex-grow: 1;
    font-size: 1em;
    line-height: 1.6;
    color: inherit; /* 继承主题默认文字颜色 */
  }

  /* 强调高亮的新闻 (Science/Nature) */
  .highlight-news {
    /* 使用 10% 透明度的品牌色作为背景 */
    /* 这样在白底是淡蓝，在黑底是深蓝，完美兼容 */
    background-color: rgba(47, 127, 147, 0.08); 
    border-left: 3px solid #2f7f93;
    padding: 15px;
    border-radius: 0 8px 8px 0;
    margin-left: -15px; /* 修正padding带来的视觉偏移 */
  }

  /* 新闻中的图片容器 */
  .news-img-box {
    margin-top: 15px;
    display: inline-block;
    padding: 5px;
    /* 图片边框和背景也使用半透明 */
    border: 1px solid rgba(128, 128, 128, 0.2);
    background: rgba(128, 128, 128, 0.05); 
    border-radius: 6px;
    transition: transform 0.2s;
  }

  .news-img-box:hover {
    transform: scale(1.02);
  }

  .news-img-box a {
    display: block;
  }

  .news-img-box img {
    display: block;
    max-width: 100%;
    height: auto;
    border-radius: 2px;
  }

  /* 多图并排：强制等高一排 */
  .news-img-box.uniform img {
    height: 150px;
    width: 100%;
    object-fit: cover;
  }

  /* --- 访客统计样式 --- */
  .footer-counter {
    margin-top: 80px;
    padding: 20px;
    /* 使用极淡的半透明背景 */
    background: rgba(128, 128, 128, 0.1);
    border-radius: 8px;
    text-align: center;
  }

  /* --- 移动端适配 --- */
  @media (max-width: 768px) {
    .news-item {
      flex-direction: column;
      gap: 5px;
    }
    .news-date {
      text-align: left;
      width: 100%;
      font-size: 0.85em;
    }
    .highlight-news {
      margin-left: 0;
    }
  }
</style>

<div class="page-container">

  <section id="about">
    <h1 class="section-heading">About Dr. Kui Wang</h1>
    
    <div class="about-content">
      <p>
        Hi, I am Kui! I was born in <a href="https://en.wikipedia.org/wiki/Jingjiang" target="_blank">Jingjiang</a> and am currently a postdoctoral researcher at the Institute of Neuroscience (<a href="http://english.cebsit.cas.cn/" target="_blank">ION</a>), Chinese Academy of Sciences (CAS), working with the support of Dr. <a href="http://www.mulab.org" target="_blank">Yu Mu</a>. Previously, I obtained my Ph.D. in Genetics from the Institute of Genetics and Developmental Biology, CAS, where I was mentored by Dr. <a href="http://lulab.genetics.ac.cn" target="_blank">Falong Lu</a>.
      </p>

      <p>
        My recent research focuses on developing <strong>Chimeric Nano Sensors (CNS)</strong> for in vivo imaging. During my doctoral studies, I introduced a novel tryptophan fluorescent protein sensor, enabling absolute quantification of tryptophan dynamics with single-cell resolution and whole-body precision (<a href="/publication/2023-10-31-Tryptophan-sensor">Cell Discovery, 2023</a>). Leveraging this sensor, we achieved quantitative imaging of tryptophan across diverse samples—including <em>E. coli</em>, mammalian cells, zebrafish, and human samples—ultimately delineating the systemic redistribution patterns of tryptophan triggered by inflammation (<a href="/publication/2024-11-14-Tryptophan-imaging">BMC Biology, 2024</a>).
      </p>

      <p>
        In response to the rising demands for simultaneous imaging of multiple physiological indicators, I collaborated with <a href="http://www.yulonglilab.org/" target="_blank">Yulong Li</a>'s group at Peking University to develop a chemogenetic infrared dopamine sensor HaloDA1.0. This innovation, when paired with a red calcium sensor and a green ATP sensor, enables the simultaneous imaging of distinct physiological indicators during epileptic states in zebrafish (<a href="/publication/2025-03-21-HaloDA">Science, 2025</a>). 
      </p>

      <p>
        To further enhance the usability and brightness of chemogenetic imaging, I partnered with <a href="https://zhixingchenlab.mysxl.cn/" target="_blank">Zhixing Chen</a>'s team at Peking University to develop BD dyes. These multi-colored chemical dyes, with improved brightness and cell permeability, are designed for seamless integration with genetically encoded indicators, enabling high-precision live imaging across various species, including zebrafish (<a href="/publication/2025-02-27-BD-Dye">Nature Methods, 2025</a>).
      </p>

      <p>
        We are currently integrating advanced technologies such as <strong>AI-assisted protein design</strong>, <strong>semi-automated high-throughput screening</strong>, <strong>rapid in vivo expression in zebrafish</strong>, and <strong>light-sheet microscopy imaging</strong> to develop next-generation optical imaging tools(e.g., Tryptamine sensor <a href="/resources/#trpa-sensor">GEM<sub>TrpA</sub>1.0</a> (<a href="/publication/2026-06-19-TrpA-sleep">Nature Neuroscience, 2026</a>), Forchlorfenuron sensor <a href="/publications/">GEM<sub>CPPU</sub>1.0</a> (ACS Synthetic Biology, in revision), among others). These efforts aim to address key scientific questions in molecular and cellular neurobiology, neuromodulation of metabolism, and neuro–tumor interactions.
      </p>
    </div>
  </section>


  <section id="news">
    <h1 class="section-heading">News & Updates</h1>
    
    <div class="news-feed">

      <div class="news-item highlight-news">
        <div class="news-date">Jun 19, 2026</div>
        <div class="news-body">
          📄 New <a href="/resources/#trpa-sensor">Tryptamine Sensor</a> paper published in <a href="/publication/2026-06-19-TrpA-sleep"><strong>Nature Neuroscience</strong></a>.
          <br>
          <div class="news-img-box">
             <a href="/images/about/TrpA_sensor.png" target="_blank">
                <img src="/images/about/TrpA_sensor.png" alt="TrpA Sensor" style="max-width: 180px; max-height: 150px; width: auto; height: auto;">
             </a>
          </div>
        </div>
      </div>



      <div class="news-item">
        <div class="news-date">May 15, 2026</div>
        <div class="news-body">
          🌿 What a wonderful time at our annual <strong>Spring Retreat</strong>!
          The team spent an unforgettable weekend hiking and relaxing in the scenic hills.
          Special thanks to everyone for making it so special.
          <br>
          <div class="news-img-box uniform" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
            <a href="/images/news/retreat1.jpg" target="_blank">
              <img src="/images/news/retreat1.jpg" alt="Spring Retreat">
            </a>
            <a href="/images/news/retreat.jpg" target="_blank">
              <img src="/images/news/retreat.jpg" alt="Spring Retreat">
            </a>
            <a href="/images/news/retreat2.jpg" target="_blank">
              <img src="/images/news/retreat2.jpg" alt="Spring Retreat">
            </a>
          </div>
        </div>
      </div>



      <div class="news-item">
        <div class="news-date">Feb 8, 2026</div>
        <div class="news-body">
          🏆 Congratulations to <a href="/Team/#Jia">Jia Qian</a> for receiving the <strong>Excellent Presentation Award</strong> at the 
          <a href="https://mp.weixin.qq.com/s/q4r7DFClAbgz0oaRi9MXkA" target="_blank">Shanghai Normal University Annual Conference</a> 
          for the report on <a href="/resources/#ado-sensor">Adenosine sensor</a> development!
          <br>
          <div class="news-img-box uniform" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
            <a href="/images/news/2026-Jia.jpg" target="_blank">
              <img src="/images/news/2026-Jia.jpg" alt="Award 1">
            </a>
            <a href="/images/news/2026-Jia2.jpg" target="_blank">
              <img src="/images/news/2026-Jia2.jpg" alt="Award 2">
            </a>
            <a href="/images/news/2026-Jia3.jpg" target="_blank">
              <img src="/images/news/2026-Jia3.jpg" alt="Award 3">
            </a>
          </div>
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Jan 17, 2026</div>
        <div class="news-body">
          👋 We are delighted to welcome <a href="/Team/#Yichen">Yang Yichen</a> from <a href="https://en.zhiyuan.sjtu.edu.cn/" target="_blank">Zhiyuan College, Shanghai Jiao Tong University</a> to join us for a winter internship!
        </div>
      </div>




      <div class="news-item">
        <div class="news-date">Nov 1, 2025</div>
        <div class="news-body">
          👋 We are pleased to welcome <a href="/Team/#Zhengyuan">Zhengyuan</a> and <a href="/Team/#Yiran">Yiran</a> to our team as post-graduate research assistants.
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Nov 2, 2025</div>
        <div class="news-body">
          🎉 Congratulations to <a href="/Team/#Yihan">Yihan</a> for winning <strong>First Prize</strong> at the <a href="https://mp.weixin.qq.com/s/Gi1v9bK5biY94kZGdkgSmA"> Undergraduate Research Forum</a> of <a href="https://qwc.shu.edu.cn/" target="_blank">Qian Weichang College</a>!
          <br>
          <div class="news-img-box uniform" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
            <a href="/images/about/yihan3.jpg" target="_blank">
              <img src="/images/about/yihan3.jpg" alt="Award">
            </a>
            <a href="/images/about/yihan2.jpg" target="_blank">
              <img src="/images/about/yihan2.jpg" alt="Award">
            </a>
            <a href="/images/about/yihan1.jpg" target="_blank">
              <img src="/images/about/yihan1.jpg" alt="Award">
            </a>
          </div>
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Oct 23, 2025</div>
        <div class="news-body">
          🎉 Congratulations to <a href="/#about">Kui</a> for receiving the <strong>Excellent <a href="/publication/2025-04-05-Trp-metab-poster">Poster</a> Award</strong> at the <a href="https://www.csbmb.org.cn/2025/eindex.html" target="_blank">2025 CSBMB Annual Symposium</a> in Nanchang.
          <br>
          <div class="news-img-box" style="display: flex; gap: 10px; flex-wrap: wrap;">
             <a href="/images/about/poster-award.jpg" target="_blank">
               <img src="/images/about/poster-award.jpg" alt="Poster Award" style="max-height: 150px; height: auto; width: auto; max-width: 100%;">
             </a>
             <a href="/images/about/poster-award2.jpg" target="_blank">
               <img src="/images/about/poster-award2.jpg" alt="Poster Award" style="max-height: 150px; height: auto; width: auto; max-width: 100%;">
             </a>
          </div>
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Sep 10, 2025</div>
        <div class="news-body">
          🎉 Congratulations to <a href="/Team/#Jia">Qian Jia</a> on winning second prize and a cash award for her thesis mid-term report!
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Aug 26, 2025</div>
        <div class="news-body">
          🏆 Great news! Our summer intern <a href="/Team/#Yun">Yun</a> took home the <strong>First Prize at the National Microbiology Competition</strong> with her piece “One Flower, One Universe.” A fantastic achievement on the national stage!
          <br>
          <div class="news-img-box">
            <a href="/images/news/One flower, one universe.gif" target="_blank">
              <img src="/images/news/One flower, one universe.gif" alt="Microbial Art" style="max-width: 200px; width: auto; height: auto;">
            </a>
          </div>
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Aug 24, 2025</div>
        <div class="news-body">
          🧪 New molecular benches installed! Ready for more experiments.
          <br>
          <div class="news-img-box">
             <a href="/images/news/benches.png" target="_blank">
               <img src="/images/news/benches.png" alt="Lab Benches" style="max-width: 100%; width: auto; height: auto;">
             </a>
          </div>
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Aug 11, 2025</div>
        <div class="news-body">
          👋 We are pleased to welcome <a href="/Team/#Lexin">Lexin</a> to our team as a summer intern.
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Jul 14, 2025</div>
        <div class="news-body">
          👋 We are pleased to welcome <a href="/Team/#Yuanhua">Yuanhua</a>, <a href="/Team/#Yihan">Yihan</a>, <a href="/Team/#Yongkang">Yongkang</a>, and <a href="/Team/#Ziyu">Ziyu</a> to our team as summer interns.
        </div>
      </div>

       <div class="news-item highlight-news">
        <div class="news-date">Jun 5, 2025</div>
        <div class="news-body">
          📄 New <a href="/publication/2025-03-21-HaloDA">Chemigenetic Dopamine Sensor</a> paper published in <strong style="color: #d10056;">Science</strong>!
          <br>
          <div class="news-img-box">
             <a href="/images/papers/HaloDA1.0.png" target="_blank">
                <img src="/images/papers/HaloDA1.0.png" alt="HaloDA Paper" style="max-width: 180px; width: auto; height: auto;">
             </a>
          </div>
        </div>
      </div>

      <div class="news-item highlight-news">
        <div class="news-date">May 20, 2025</div>
        <div class="news-body">
          📄 New <a href="/publication/2025-02-27-BD-Dye">Chemigenetic Dyes</a> paper published in <strong>Nature Methods</strong>.
          <br>
          <div class="news-img-box">
             <a href="/images/papers/BD-dye.png" target="_blank">
                <img src="/images/papers/BD-dye.png" alt="BD Dye" style="max-width: 180px; width: auto; height: auto;">
             </a>
          </div>
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">May 14, 2025</div>
        <div class="news-body">
          👋 We are pleased to welcome <a href="/Team/#Jia">Jia Qian</a> to our team. She joins us to complete her undergraduate thesis research.
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Apr 7, 2025</div>
        <div class="news-body">
          📊 Presented a poster on <a href="/publication/2025-04-05-Trp-metab-poster">Tryptophan metabolism</a> at <a href="https://cell-press-symposia.com/neurometabolism-2025/conference-program.html" target="_blank">Cell Symposia</a> in Shenzhen.
        </div>
      </div>

      <div class="news-item highlight-news">
        <div class="news-date">Nov 14, 2024</div>
        <div class="news-body">
          📄 New <a href="/publication/2024-11-14-Tryptophan-imaging">Tryptophan imaging</a> paper published in <strong>BMC Biology</strong>.
          <br>
          <div class="news-img-box">
             <a href="/images/papers/trp.png" target="_blank">
                <img src="/images/papers/trp.png" alt="BMC Paper" style="max-width: 180px; width: auto; height: auto;">
             </a>
          </div>
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Dec 31, 2024</div>
        <div class="news-body">
          📊 Presented a poster about <a href="/publication/2024-09-30-CaLAMP-poster">Bioluminescent Imaging</a> at <a href="https://www.cns.org.cn/2024/cn-index.html" target="_blank">CNS-2024</a> in Suzhou.
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Jan 1, 2024</div>
        <div class="news-body">
          🚀 Started my PostDoc at <a href="http://www.mulab.org" target="_blank">Mu Lab</a> in <a href="http://english.cebsit.cas.cn/" target="_blank">ION</a>.
        </div>
      </div>

      <div class="news-item  highlight-news">
        <div class="news-date">Oct 31, 2023</div>
        <div class="news-body">
          📄 New <a href="/publication/2023-10-31-Tryptophan-sensor">Fluorescent Tryptophan Sensor</a> paper published in <strong>Cell Discovery</strong>.
          <br>
          <div class="news-img-box">
             <a href="/images/papers/Cell Disc_Logo.jpg" target="_blank">
                <img src="/images/papers/Cell Disc_Logo.jpg" alt="Cell Discovery" style="max-width: 180px; width: auto; height: auto;">
             </a>
          </div>
        </div>
      </div>
      
       <div class="news-item">
        <div class="news-date">Sep 19, 2023</div>
        <div class="news-body">
           📜 Patent for Tryptophan sensor <a href="/publication/tryptamine-sensor-patent/" target="_blank">GRIT</a> announced in China.
        </div>
      </div>

      <div class="news-item">
        <div class="news-date">Sep 18, 2023</div>
        <div class="news-body">
          🎓 Thrilled to pass my Ph.D. Defense in Beijing. 🎉🎉🎉
        </div>
      </div>

    </div>
  </section>

  <div class="footer-counter">
    <a href="https://info.flagcounter.com/b5Gl"><img src="https://s01.flagcounter.com/map/b5Gl/size_l/txt_000000/border_CCCCCC/pageviews_1/viewers_0/flags_1/" alt="Free counters!" border="0"></a>
  </div>



  {% if site.disqus.shortname %}
    <div style="margin-top: 50px;">
      <div id="disqus_thread"></div>
      <script>
        var disqus_config = function () {
          this.page.url = '{{ page.url | absolute_url }}';
          this.page.identifier = '{{ page.id }}';
        };
        (function() {
          var d = document, s = d.createElement('script');
          s.src = 'https://{{ site.disqus.shortname }}.disqus.com/embed.js';
          s.setAttribute('data-timestamp', +new Date());
          (d.head || d.body).appendChild(s);
        })();
      </script>
      <noscript>Please enable JavaScript to view the comments.</noscript>
    </div>
  {% endif %}

</div>