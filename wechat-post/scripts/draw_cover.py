#!/usr/bin/env python3
"""封面图绘制脚本 - PIL 叠加 AI 生图背景 + 文字

封面设计规范（来自 wechat-post skill v1.18）：
- 尺寸：900 × 383 px
- 背景：ai-image-gen 生成的水彩场景图（拉伸铺满）
- 文字区：右下角，黑色半透明卡片衬底（alpha=128，约50%不透明度）
- 文字：主标题 80px，副标题 32px
- 配色：BG=(13,27,42)，ACCENT=(255,145,40)，WHITE，GRAY=(215,215,225)
- 中文字体：/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc

字数限制（v1.18，硬性规则）：
- LINE1（大字第一行）：≤ 5 个字符
- LINE2（大字第二行）：≤ 5 个字符
- SUBTEXT（副标题）：10 – 13 个字符
- 超出会被截断，且无法在图片内发现，必须在下发前自查

使用说明：
- 第一步：用 ai-image-gen skill 生成背景图，保存为 cover_bg.png
- 第二步：设置 BG_IMAGE、LINE1（≤5字）、LINE2（≤5字）、SUBTEXT（≤13字），运行本脚本
- 第三步：运行后验证图片，检查文字是否完整显示
- 注意：输出路径使用 expanduser("~/.hermes/research/imgs")，不受工作目录影响
"""
from PIL import Image, ImageDraw, ImageFont
import os

# ========== 可配置参数 ==========
BG_IMAGE = "/home/ubuntu/.hermes/research/imgs/cover_bg.png"

TEXT_X    = 460
TEXT_TOP  = 55
CARD_PX   = 20
LINE1     = "够用了"
LINE2     = "不再死磕"
SUBTEXT   = "只追够用的解"

W, H = 900, 383
BG      = (13, 27, 42)
ACCENT  = (255, 145, 40)
WHITE   = (255, 255, 255)
GRAY    = (215, 215, 225)
# ==================================

# 底层：背景图 or 纯色
img = Image.new("RGB", (W, H), BG)
if BG_IMAGE:
    bg_path = os.path.expanduser(BG_IMAGE)
    if os.path.exists(bg_path):
        bg = Image.open(bg_path).convert("RGB").resize((W, H), Image.LANCZOS)
        img = bg

draw = ImageDraw.Draw(img)

# --- 文字区黑色半透明卡片 ---
# 卡片范围：从 TEXT_X - CARD_PX 到 右边缘，上下包住三行文字
card_left   = TEXT_X - CARD_PX
card_right  = W
# 根据80px字体计算文字高度：LINE1(80) + 间距(10) + LINE2(80) + 间距(10) + SUBTEXT(32) + 留白
card_top    = TEXT_TOP - 15
card_bottom = TEXT_TOP + 80 + 10 + 80 + 10 + 32 + 20
card_height = card_bottom - card_top

# 叠加白色半透明层（用 RGBA 模式画矩形）
img_rgba = img.convert("RGBA")
overlay  = Image.new("RGBA", (W, H), (0, 0, 0, 0))
card_draw = ImageDraw.Draw(overlay)

# 黑色半透明矩形（alpha=128，约50%不透明度）
card_draw.rectangle(
    [(card_left, card_top), (card_right, card_bottom)],
    fill=(0, 0, 0, 128)
)

img_rgba = Image.alpha_composite(img_rgba, overlay)
img = img_rgba.convert("RGB")
draw = ImageDraw.Draw(img)

# --- 左侧细渐变（氛围感）---
for i in range(60):
    alpha = int(50 * (1 - i / 60))
    draw.line([(0, i), (0, H - i)], fill=BG)

# --- 竖线装饰 ---
draw.line(
    [(card_left + 8, card_top + 5), (card_left + 8, card_bottom - 5)],
    fill=ACCENT, width=3
)

# --- 文字 ---
font_path  = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
font_large = ImageFont.truetype(font_path, 80)
font_sub   = ImageFont.truetype(font_path, 32)

draw.text((TEXT_X, TEXT_TOP),      LINE1,   font=font_large, fill=WHITE)
draw.text((TEXT_X, TEXT_TOP + 90),  LINE2,   font=font_large, fill=ACCENT)
draw.text((TEXT_X, TEXT_TOP + 185), SUBTEXT, font=font_sub,   fill=GRAY)

# --- 保存 ---
out_dir  = os.path.expanduser("~/.hermes/research/imgs")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "cover.png")
img.save(out_path, "PNG")
print(f"封面已保存: {out_path}")
