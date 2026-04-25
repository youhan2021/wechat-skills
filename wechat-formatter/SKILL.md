---
name: wechat-formatter
description: 微信公众号 HTML 排版——读取 markdown + media_id 构建 HTML 草稿、执行 create-draft
triggers:
  - "生成公众号草稿"
  - "公众号排版"
env:
  WECHAT_API_SCRIPT: ~/.hermes/skills/wechat-api-lite/scripts/wechat_api.py
  RESEARCH_DIR: ~/.hermes/research/
---

# 微信公众号 HTML 排版

## 重要前提

- **正文必须先通过相似度检查，图片必须先上传完成，才能构建 HTML**
- 不满足条件不构建草稿

## 格式规范

### 字号（已更新为最新）

| 元素 | 字号 | 其他 |
|---|---|---|
| 小标题 h2 | 16px | 蓝色 #3A5CCC，底部浅橙分隔线 |
| 三级标题 h3 | 15px | 橙色 #c2460a |
| 正文段落 | 14px | 行高 1.9，段落间距 14px |
| 代码块 pre | 13px | 深色背景 #1a1a2e |
| 图注 | 13px | 灰色 #999，居中 |

### HTML 内联样式（全文必须用内联 style）

```html
<!-- 小标题 -->
<h2 style="font-size:16px;font-weight:bold;color:#3A5CCC;margin:28px 0 10px;padding-bottom:8px;border-bottom:2px solid #f5c89a;">❶ 小标题句子</h2>

<!-- 正文段落 -->
<p style="font-size:14px;line-height:1.9;color:#333;margin:14px 0;">正文内容，每段3-4行，禁止一行一句</p>

<!-- 高亮 -->
<strong style="color:#3A5CCC;font-weight:bold;">【关键词】</strong>正文

<!-- 配图 -->
<img style="display:block;max-width:640px;width:100%;margin:18px auto;border-radius:10px;" src="FIG_URL" />
<p style="font-size:13px;color:#999;text-align:center;margin-top:6px;margin-bottom:18px;">图注（来自文章已有句子）</p>

<!-- 结尾分隔线 -->
<hr style="border:none;border-top:2px solid #f5c89a;margin:28px 0 14px;" />

<!-- 结尾弱化（单独成段，不突出） -->
<p style="font-size:13px;color:#555;">这个 skill 现在已经放到 ClawHub 了，名字是 bazi-lookup。</p>
```

### 正文换行规则

- **每段 3~4 行**，禁止过短的单句段落
- 枚举内容合并成一行用顿号连接
- 禁止一行一句

### 高亮规范

- 全文精简到 6-8 句核心判断句
- 用 `<strong style="color:#3A5CCC;font-weight:bold;">` 包住
- **禁止写 `**文字**`**（Markdown 语法在 HTML 里原样显示）

### 结尾弱化

- ClawHub 句式单独成段
- 与正文结尾空两行
- 语气自然，不突出、不像推广

---

## 构建 HTML 草稿

### Step 1: 读取 markdown 文件

```python
import re

with open('/home/ubuntu/.hermes/research/article_xxx.md') as f:
    md = f.read()
```

### Step 2: 解析 markdown 生成 HTML

```python
lines = md.split('\n')
html = []
i = 0

while i < len(lines):
    line = lines[i].strip()

    # 跳过空行
    if not line:
        i += 1
        continue

    # h2 小标题（❶❷❸格式）
    m = re.match(r'^## (.+)', line)
    if m:
        title = m.group(1).strip()
        html.append(f'<h2 style="font-size:16px;font-weight:bold;color:#3A5CCC;margin:28px 0 10px;padding-bottom:8px;border-bottom:2px solid #f5c89a;">{title}</h2>')
        # ❶标题出现后立即插fig1，❷出现后插fig2...
        # （在下面配图插入节统一处理）
        i += 1
        continue

    # h3 三级标题
    m = re.match(r'^### (.+)', line)
    if m:
        title = m.group(1).strip()
        html.append(f'<h3 style="font-size:15px;font-weight:bold;color:#c2460a;margin:22px 0 8px;">{title}</h3>')
        i += 1
        continue

    # 段落（普通文字行）
    # 收集连续的文字行，合并成一个段落
    para_lines = []
    while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('#'):
        para_lines.append(lines[i].strip())
        i += 1
    if para_lines:
        text = ' '.join(para_lines)
        # 处理高亮 【关键词】
        text = re.sub(r'【([^】]+)】', 
            r'<strong style="color:#3A5CCC;font-weight:bold;">【\1】</strong>',
            text)
        html.append(f'<p style="font-size:14px;line-height:1.9;color:#333;margin:14px 0;">{text}</p>')
    continue

content = '\n'.join(html)
```

### Step 3: 插入配图（h2 触发方式）

```python
# 配图 URL（从 wechat-post-image 获取）
FIG1_URL = "https://mmbiz.qpic.cn/..."
FIG2_URL = "https://mmbiz.qpic.cn/..."

# 在 h2 标签后插入
final_html = content

# 方法：用精确字符串定位，在下一个小标题前插入
# 例如：❷ 出现时，说明❶节结束，在❶的最后一个段落后插fig1
# 在 emit h2 时检查下一个标题来触发配图插入

def insert_figs(html_content, fig1_url, fig2_url):
    lines = html_content.split('\n')
    result = []
    pending_fig1 = False
    pending_fig2 = False

    for line in lines:
        result.append(line)
        # ❶标题出现 → 标记，等待❷出现时插fig1
        if '<h2' in line and '❶' in line:
            pending_fig1 = True
        # ❷标题出现 → ❶节结束，插fig1
        elif '<h2' in line and '❷' in line and pending_fig1:
            result.append(f'<img style="display:block;max-width:640px;width:100%;margin:18px auto;border-radius:10px;" src="{fig1_url}" />')
            result.append(f'<p style="font-size:13px;color:#999;text-align:center;margin-top:6px;margin-bottom:18px;">图注（来自文章已有句子）</p>')
            pending_fig1 = False
        # ❸标题出现 → ❷节结束，插fig2
        elif '<h2' in line and '❸' in line:
            if pending_fig2:
                # ❷节也有fig
                pass
            pending_fig2 = True
        # ❹标题出现 → ❷/❸节结束
        elif '<h2' in line and '❹' in line and pending_fig2:
            result.append(f'<img style="display:block;max-width:640px;width:100%;margin:18px auto;border-radius:10px;" src="{fig2_url}" />')
            result.append(f'<p style="font-size:13px;color:#999;text-align:center;margin-top:6px;margin-bottom:18px;">图注</p>')
            pending_fig2 = False

    return '\n'.join(result)
```

### Step 4: 写入 draft.json

```python
import json

draft = [{
    "title": "文章标题",
    "author": "Youhan",
    "thumb_media_id": "COVER_MEDIA_ID",  # 封面 media_id
    "content": final_html
}]

with open('/home/ubuntu/.hermes/research/draft.json', 'w') as f:
    json.dump(draft, f, ensure_ascii=False)
```

### Step 5: 执行 create-draft

```bash
python3 ~/.hermes/skills/wechat-api-lite/scripts/wechat_api.py create-draft ~/.hermes/research/draft.json
```

---

## 常见错误

| 错误 | 结果 | 正确做法 |
|---|---|---|
| 用 `<style>` 标签 | 格式完全不生效 | 全文用内联 `style` 属性 |
| draft.json 用 `{}` 对象 | API 返回格式错误 | 必须用 `[{"title":..., "content":...}]` 数组 |
| 本地文件名做 src | 配图显示空白 | 必须用上传后的微信 URL |
| 段落过短一行一句 | 文章读起来碎 | 每段 3-4 行合并 |
| 高亮 phrase 含换行符 | 高亮失败 | 含 `\n` 的多行 phrase 单独处理 |

---

## 交付

完成后输出：
```
---
草稿 media_id：[media_id]
封面：描述
配图：描述
---
```
