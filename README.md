# SMS-Bomber-Sender
SMS Sender - Professional PyQt6 Application

A powerful and user-friendly SMS Sender application built with Python and PyQt6, designed to automate sending SMS requests to multiple services. This cross-platform desktop application features a modern Windows 11-style interface with dark mode, a progress bar, and detailed logging. Ideal for developers, testers, and automation enthusiasts looking for a robust tool to manage SMS-based operations.

Table of Contents

Features Installation Usage Screenshots Supported Services Contributing License Contact

Features

Modern UI: Sleek Windows 11-style interface with dark mode using qdarkstyle. Multi-Service Support: Send SMS requests to over 40 services like Snapp, AliBaba, Divar, and more. Threaded Requests: Asynchronous request handling with progress tracking using QThread. Customizable: Enable/disable services via checkboxes and set iteration counts. Error Handling: Robust logging and error management for reliable operation. Cross-Platform: Runs on Windows, macOS, and Linux. Multilingual: Documentation in English, Persian, and Chinese.

Installation Prerequisites

Python: Version 3.8 or higher PyQt6: For the graphical interface requests: For HTTP requests qdarkstyle: For the dark theme Operating System: Windows, macOS, or Linux

Steps

Create a Virtual Environment (recommended): python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate

Install Dependencies: pip install pyqt6 requests qdarkstyle

Run the Application: python main.py

Usage

Launch the Application:Run main.py to open the GUI. Enter Phone Number:Input a 10-digit phone number (e.g., 9123456789). Select Services:Check the boxes for the services you want to send SMS requests to. Set Iterations:Use the spin box to specify the number of request iterations. Start Sending:Click the "Start" button to begin sending requests. Monitor progress via the progress bar and logs. Stop or Clear:Use the "Stop" button to halt the process or "Clear Log" to reset the log output.

Note: Ensure you have an active internet connection and comply with the terms of service for each platform.

Screenshots Add screenshots or GIFs of the application in action here to showcase the interface and functionality.

Supported Services The application supports sending SMS requests to the following services:

Snapp AliBaba Divar Tapsi eCharge Pikato And 35+ more! (See the full list in the code)

Contributing Contributions are welcome! To contribute:

Fork the repository. Create a new branch (git checkout -b feature/your-feature). Make your changes and commit (git commit -m 'Add your feature'). Push to the branch (git push origin feature/your-feature). Open a Pull Request.

Please ensure your code follows PEP 8 standards and includes appropriate documentation.

======================================================================================

SMS Sender - رابط کاربری حرفه‌ای با PyQt6 

یک برنامه قدرتمند و کاربرپسند برای ارسال پیامک، ساخته شده با پایتون و PyQt6، که برای خودکارسازی ارسال درخواست‌های پیامکی به سرویس‌های مختلف طراحی شده است. این برنامه دسکتاپ با رابط کاربری مدرن به سبک ویندوز ۱۱، حالت تیره، نوار پیشرفت و لاگ‌های دقیق ارائه می‌شود. این ابزار برای توسعه‌دهندگان، آزمایش‌کنندگان و علاقه‌مندان به خودکارسازی مناسب است.

فهرست مطالب

ویژگی‌ها نصب نحوه استفاده تصاویر سرویس‌های پشتیبانی‌شده مشارکت مجوز تماس

ویژگی‌ها

رابط کاربری مدرن: طراحی شیک به سبک ویندوز ۱۱ با حالت تیره با استفاده از qdarkstyle. پشتیبانی از چندین سرویس: ارسال درخواست‌های پیامکی به بیش از ۴۰ سرویس مانند اسنپ، علی‌بابا، دیوار و غیره. درخواست‌های چندنخی: مدیریت ناهمزمان درخواست‌ها با پیگیری پیشرفت از طریق QThread. قابلیت سفارشی‌سازی: فعال/غیرفعال کردن سرویس‌ها از طریق چک‌باکس‌ها و تنظیم تعداد تکرارها. مدیریت خطاها: لاگ‌گیری و مدیریت خطاهای قوی برای عملکرد مطمئن. چندسکویی: قابل اجرا در ویندوز، مک‌او‌اس و لینوکس. چندزبانه: مستندات به زبان‌های انگلیسی، فارسی و چینی.

نصب پیش‌نیازها

پایتون: نسخه ۳.۸ یا بالاتر PyQt6: برای رابط گرافیکی requests: برای درخواست‌های HTTP qdarkstyle: برای تم تیره سیستم‌عامل: ویندوز، مک‌او‌اس یا لینوکس

مراحل


ایجاد محیط مجازی (توصیه می‌شود): python -m venv venv source venv/bin/activate # در ویندوز: venv\Scripts\activate

نصب وابستگی‌ها: pip install pyqt6 requests qdarkstyle

اجرای برنامه: python main.py

نحوه استفاده

اجرای برنامه:فایل main.py را اجرا کنید تا رابط گرافیکی باز شود. وارد کردن شماره تلفن:یک شماره تلفن ۱۰ رقمی وارد کنید (مثلاً 9123456789). انتخاب سرویس‌ها:چک‌باکس‌های مربوط به سرویس‌هایی که می‌خواهید درخواست پیامکی ارسال کنید را علامت بزنید. تنظیم تعداد تکرارها:از اسپین‌باکس برای تعیین تعداد تکرار درخواست‌ها استفاده کنید. شروع ارسال:روی دکمه "شروع" کلیک کنید تا فرآیند ارسال آغاز شود. پیشرفت را از طریق نوار پیشرفت و لاگ‌ها مشاهده کنید. توقف یا پاک کردن:از دکمه "توقف" برای متوقف کردن فرآیند یا "پاک کردن لاگ" برای بازنشانی خروجی لاگ استفاده کنید.

توجه: اطمینان حاصل کنید که اتصال اینترنت فعال دارید و با شرایط سرویس هر پلتفرم رعایت می‌کنید.

تصاویر تصاویر یا GIFهایی از عملکرد برنامه را اینجا اضافه کنید تا رابط کاربری و عملکرد آن نمایش داده شود.

سرویس‌های پشتیبانی‌شده این برنامه از ارسال درخواست‌های پیامکی به سرویس‌های زیر پشتیبانی می‌کند:

اسنپ علی‌بابا دیوار تاپسی ای‌چارج پیکاتو و بیش از ۳۵ سرویس دیگر! (لیست کامل را در کد مشاهده کنید)

مشارکت مشارکت‌ها استقبال می‌شوند! برای مشارکت:

مخزن را فورک کنید. شاخه جدیدی ایجاد کنید (git checkout -b feature/your-feature). تغییرات خود را اعمال و کامیت کنید (git commit -m 'Add your feature'). به شاخه ارسال کنید (git push origin feature/your-feature). یک Pull Request باز کنید.

لطفاً مطمئن شوید که کد شما مطابق با استانداردهای PEP 8 است و مستندات مناسبی دارد.
===============================================================================================
SMS Sender - 使用 PyQt6 的专业界面 

一个功能强大且用户友好的 SMS Sender 应用程序，使用 Python 和 PyQt6 构建，旨在自动化向多个服务发送短信请求。这款跨平台桌面应用程序具有现代 Windows 11 风格的界面，支持暗黑模式、进度条和详细日志记录。适合开发人员、测试人员和自动化爱好者使用，管理基于短信的操作。

目录

功能 安装 使用方法 截图 支持的服务 贡献 许可证 联系方式

功能

现代化界面: 使用 qdarkstyle 实现的 Windows 11 风格暗黑模式界面。 多服务支持: 向超过 40 个服务（如 Snapp、AliBaba、Divar 等）发送短信请求。 异步请求: 使用 QThread 进行异步请求处理，带进度跟踪。 可定制化: 通过复选框启用/禁用服务并设置迭代次数。 错误处理: 强大的日志记录和错误管理，确保可靠运行。 跨平台: 支持 Windows、macOS 和 Linux。 多语言支持: 提供英文、波斯语和中文文档。

安装 前提条件

Python: 版本 3.8 或更高 PyQt6: 用于图形界面 requests: 用于 HTTP 请求 qdarkstyle: 用于暗黑主题 操作系统: Windows、macOS 或 Linux

步骤

创建虚拟环境 (推荐): python -m venv venv source venv/bin/activate # 在 Windows 上: venv\Scripts\activate

安装依赖: pip install pyqt6 requests qdarkstyle

运行应用程序: python main.py

使用方法

启动应用程序:运行 main.py 以打开图形界面。 输入电话号码:输入 10 位电话号码（例如 9123456789）。 选择服务:勾选您希望发送短信请求的服务的复选框。 设置迭代次数:使用旋转框指定请求的迭代次数。 开始发送:点击“开始”按钮以启动请求发送。通过进度条和日志监控进度。 停止或清除:使用“停止”按钮暂停进程，或使用“清除日志”重置日志输出。

注意: 确保有活跃的互联网连接，并遵守每个平台的条款。

截图 在此处添加应用程序运行时的截图或 GIF，以展示界面和功能。

支持的服务 该应用程序支持向以下服务发送短信请求：

Snapp AliBaba Divar Tapsi eCharge Pikato 以及 35+ 其他服务！（在代码中查看完整列表）

贡献 欢迎贡献！要参与：

叉取仓库。 创建新分支 (git checkout -b feature/your-feature)。 进行更改并提交 (git commit -m 'Add your feature')。 推送到分支 (git push origin feature/your-feature)。 打开 Pull Request。

请确保您的代码遵循 PEP 8 标准并包含适当的文档。

