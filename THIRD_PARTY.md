# Third-Party Sources

本仓库包含自编脚本与自定义规则整理逻辑，同时引用外部规则项目作为上游来源。

## 1. Loyalsoldier / clash-rules

- Project: [https://github.com/Loyalsoldier/clash-rules](https://github.com/Loyalsoldier/clash-rules)
- Used for:
  - `applications`
  - `private`
  - `direct`
  - `lancidr`
  - `cncidr`
- Local usage in this repository:
  - referenced in documentation
  - fetched by `scripts/sync_loyalsoldier.ps1`
  - referenced by generated or merged Mihomo configuration as remote rule providers

## 2. What this repository does not bundle by default

为减少许可证混淆，本仓库默认不直接提交上述上游规则文件内容。

仓库公开内容主要包括：

- 自定义直连规则
- 规则构建脚本
- 订阅合并脚本
- 使用说明

## 3. Licensing note

本仓库的 MIT 许可证仅覆盖：

- 仓库作者编写的脚本
- 仓库作者编写的说明文档
- 仓库作者整理的自定义规则结构

第三方规则文件及其衍生分发方式，不自动转为 MIT；其许可证与使用条件以原项目为准。

