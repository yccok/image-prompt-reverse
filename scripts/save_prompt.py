#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
save_prompt.py — 将反推提示词保存为独立 txt 文件。

每次运行都生成一个新文件，不覆盖、不追加旧文件；文件名带时间戳，保证唯一。

用法：
  # 方式 1：从内容文件读取
  python save_prompt.py --type "人像" --content-file prompt.txt

  # 方式 2：从标准输入读取
  echo "提示词内容" | python save_prompt.py --type "产品"

  # 方式 3：直接传内容（适合较短文本）
  python save_prompt.py --type "风景" --content "0-任务目标：..."

可选：
  --outdir  指定输出目录（默认：当前工作目录下的 outputs/）

输出：
  成功时向 stdout 打印保存文件的绝对路径。
"""

import argparse
import os
import re
import sys
from datetime import datetime

DEFAULT_OUTDIR = os.path.join(os.getcwd(), "outputs")


def sanitize(name: str) -> str:
    """清理类型名中的非法文件名字符。"""
    name = (name or "").strip() or "未分类"
    name = re.sub(r'[\\/:*?"<>|\s]+', "_", name)
    return name.strip("_") or "未分类"


def unique_path(outdir: str, type_tag: str, ext: str = ".txt") -> str:
    """生成不冲突的文件路径：YYYYMMDD_HHMMSS_<类型>_<序号>.txt"""
    os.makedirs(outdir, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    idx = 1
    while True:
        fname = f"{stamp}_{type_tag}_{idx:02d}{ext}"
        path = os.path.join(outdir, fname)
        if not os.path.exists(path):
            return path
        idx += 1


def main() -> int:
    ap = argparse.ArgumentParser(description="保存反推提示词为独立 txt 文件")
    ap.add_argument("--type", default="未分类", help="图片类型，用于文件名")
    ap.add_argument("--content", default=None, help="提示词全文")
    ap.add_argument("--content-file", default=None, help="存放提示词全文的文件路径")
    ap.add_argument("--outdir", default=DEFAULT_OUTDIR, help="输出目录")
    args = ap.parse_args()

    if args.content_file:
        with open(args.content_file, "r", encoding="utf-8") as f:
            content = f.read()
    elif args.content is not None:
        content = args.content
    else:
        content = sys.stdin.read()

    if not content or not content.strip():
        print("ERROR: 内容为空，未保存。", file=sys.stderr)
        return 1

    path = unique_path(args.outdir, sanitize(args.type))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
