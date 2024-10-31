import 'package:app1/atomic/models/Prompt.dart';
import 'package:flutter/material.dart';

class MolChat extends StatelessWidget {
  final Prompt prompt;

  const MolChat({Key? key, required this.prompt}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final alignment = prompt.isUserMessage
        ? CrossAxisAlignment.end
        : CrossAxisAlignment.start;
    final color = prompt.isUserMessage ? Colors.blue[100] : Colors.grey[200];
    final textColor = prompt.isUserMessage ? Colors.black : Colors.black87;

    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 8.0, vertical: 4.0),
      child: Column(
        crossAxisAlignment: alignment,
        children: [
          Container(
            padding: const EdgeInsets.all(12.0),
            decoration: BoxDecoration(
              color: color,
              borderRadius: BorderRadius.circular(12),
            ),
            child: Text(
              prompt.text,
              style: TextStyle(color: textColor),
            ),
          ),
        ],
      ),
    );
  }
}
