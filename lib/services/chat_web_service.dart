import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'package:web_socket_client/web_socket_client.dart';

class ChatWebService {
  // Singleton pattern to ensure only one instance of the service is used
  static final _instance = ChatWebService._internal(); //holds instance of ChatWebService and initialized using a private named constructor
  WebSocket? _socket;

  factory ChatWebService() => _instance;

  ChatWebService._internal();

  // Controllers for streaming search results and content responses
  final _searchResultController = StreamController<Map<String, dynamic>>();
  final _contentController = StreamController<Map<String, dynamic>>();

  // Streams to provide real-time updates to listeners
  Stream<Map<String, dynamic>> get searchResultStream =>
      _searchResultController.stream;
  Stream<Map<String, dynamic>> get contentStream => _contentController.stream;

  // Method to connect to WebSocket server
  void connect() {
    _socket = WebSocket(Uri.parse("ws://localhost:8000/ws/chat"));

    // Listen for incoming messages from the server
    _socket!.messages.listen((message) {
      final data = json.decode(message);

      // Handling different types of responses from the server
      if (data['type'] == 'search_result') {
        _searchResultController.add(data);
      } else if (data['type'] == 'content') {
        _contentController.add(data);
      }
    });
  }

  // Method to send chat queries to the server
  void chat(String query) {
    print(query);
    print(_socket);
    _socket!.send(json.encode({'query': query}));
  }
}
