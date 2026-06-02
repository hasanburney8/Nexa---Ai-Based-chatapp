import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:nexa/services/chat_web_service.dart';
import 'package:nexa/theme/colors.dart';

import '../widgets/search_section.dart';
import '../widgets/side_bar.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  void initState() {
    super.initState();
    ChatWebService().connect(); // Connect WebSocket on startup
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Row(
          children: [
            kIsWeb ? SideBar() : SizedBox(),
            Expanded(
              child: Padding(
                padding: !kIsWeb ? const EdgeInsets.all(8.0) : EdgeInsets.zero,
                child: Column(
                  children: [
                    Expanded(
                      child: SearchSection(), // Search UI
                    ),

                    // Footer Section
                    Container(
                      padding: EdgeInsets.symmetric(vertical: 16),
                      child: Wrap(
                        alignment: WrapAlignment.center,
                        children: [
                          _footerItem("Pro"),
                          _footerItem("Enterprise"),
                          _footerItem("Store"),
                          _footerItem("Blog"),
                          _footerItem("Careers"),
                          _footerItem("English (English)"),
                        ],
                      ),
                    )
                  ],
                ),
              ),
            )
          ],
        ));
  }

  // Helper method to create footer text items
  Widget _footerItem(String text) {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: 12),
      child: Text(
        text,
        style: TextStyle(
          fontSize: 14,
          color: AppColors.footerGrey,
        ),
      ),
    );
  }
}
