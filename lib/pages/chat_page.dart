import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:nexa/widgets/answer_section.dart';
import 'package:nexa/widgets/sources_section.dart';

import '../theme/colors.dart';
import '../widgets/side_bar.dart';

class ChatPage extends StatelessWidget {
  final String question;
  const ChatPage({super.key, required this.question});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          kIsWeb ? SideBar() : SizedBox(),
          kIsWeb ? const SizedBox(width: 100) : SizedBox(),
          Expanded(
            child: SingleChildScrollView(
              child: Padding(
                padding: const EdgeInsets.all(24.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(question, style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold)),
                    SizedBox(height: 24),
                    SourcesSection(),
                    SizedBox(height: 24),
                    AnswerSection(),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
