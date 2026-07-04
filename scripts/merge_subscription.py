import argparse
from pathlib import Path

from build_overlay import PROVIDERS, load_custom_rules, render_rule_providers


def fmt_list(items, indent):
    return "".join(f"{indent}- {item}\n" for item in items)


def build_proxy_groups(proxy_names: list[str]) -> str:
    groups = "proxy-groups:\n"
    groups += "  - name: 代理模式\n"
    groups += "    type: select\n"
    groups += "    proxies:\n"
    groups += "      - 绕过大陆丨白名单(Whitelist)\n"
    groups += "      - 绕过大陆丨黑名单(GFWlist)\n\n"
    groups += "  - name: 节点选择\n"
    groups += "    type: select\n"
    groups += "    proxies:\n"
    groups += fmt_list(proxy_names + ["DIRECT"], "      ")
    groups += "\n"
    groups += "  - name: PROXY\n"
    groups += "    type: select\n"
    groups += "    proxies:\n"
    groups += fmt_list(proxy_names + ["DIRECT"], "      ")
    groups += "\n"
    groups += "  - name: 绕过大陆丨黑名单(GFWlist)\n"
    groups += "    type: select\n"
    groups += "    proxies:\n"
    groups += "      - DIRECT\n\n"
    groups += "  - name: 绕过大陆丨白名单(Whitelist)\n"
    groups += "    type: select\n"
    groups += "    proxies:\n"
    groups += "      - PROXY\n"
    return groups


def build_rules() -> str:
    custom_rules = load_custom_rules()
    lines = ["rules:\n"]
    for rule in custom_rules:
        lines.append(f"  - {rule}\n")
    lines.extend(
        [
            "  - RULE-SET,applications,DIRECT\n",
            "  - RULE-SET,private,DIRECT\n",
            "  - RULE-SET,direct,DIRECT\n",
            "  - RULE-SET,lancidr,DIRECT,no-resolve\n",
            "  - RULE-SET,cncidr,DIRECT,no-resolve\n",
            "  - GEOIP,LAN,DIRECT,no-resolve\n",
            "  - GEOIP,CN,DIRECT,no-resolve\n",
            "  - MATCH,代理模式\n",
        ]
    )
    return "".join(lines)


def merge(base_path: Path, output_path: Path, rules_base_url: str) -> None:
    text = base_path.read_text(encoding="utf-8")

    proxy_start = text.find("\nproxies:\n")
    groups_start = text.find("\nproxy-groups:\n")
    rules_start = text.find("\nrules:\n", groups_start if groups_start != -1 else 0)
    if proxy_start == -1:
        raise SystemExit("expected proxies block not found")
    if groups_start == -1 or rules_start == -1:
        raise SystemExit("expected proxy-groups/rules blocks not found")

    prefix = text[:proxy_start]
    proxies_block = text[proxy_start + 1 : groups_start]

    proxy_names = []
    for line in proxies_block.splitlines():
        stripped = line.strip()
        if stripped.startswith("- name: "):
            proxy_names.append(stripped[len("- name: ") :])

    out = prefix
    if out and not out.endswith("\n"):
        out += "\n"
    out += proxies_block.rstrip() + "\n\n"
    out += render_rule_providers(rules_base_url) + "\n"
    out += build_proxy_groups(proxy_names) + "\n"
    out += build_rules()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(out, encoding="utf-8")
    print(f"wrote {output_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, help="Base subscription yaml path")
    parser.add_argument("--output", required=True, help="Merged subscription yaml path")
    parser.add_argument(
        "--rules-base-url",
        default="https://083105.xyz/rules/loyalsoldier",
        help="Base URL for self-hosted Loyalsoldier rule files",
    )
    args = parser.parse_args()
    merge(Path(args.base), Path(args.output), args.rules_base_url)


if __name__ == "__main__":
    main()

