import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
// Ensure you have url_launcher in your pubspec.yaml for launching URLs
import 'package:url_launcher/url_launcher.dart';

class RecordsScreen extends StatelessWidget {
  const RecordsScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    FirebaseFirestore firestore = FirebaseFirestore.instance;
    CollectionReference recordsRef = firestore.collection('records');

    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 31, 35, 39),
      body: SingleChildScrollView(
        child: Column(
          children: [
            SafeArea(
              child: Align(
                alignment: Alignment.topLeft,
                child: IconButton(
                  icon: const Icon(Icons.arrow_back, color: Colors.white),
                  onPressed: () => Navigator.of(context).pop(),
                ),
              ),
            ),
            Center(
              child: Image.network(
                'https://i.ibb.co/VMxWZPW/logo.png',
                width: 150,
                height: 150,
                errorBuilder: (context, error, stackTrace) {
                  return const Text('Image not found',
                      style: TextStyle(color: Colors.white));
                },
              ),
            ),
            const SizedBox(height: 32),
            StreamBuilder<QuerySnapshot>(
              stream: recordsRef.snapshots(),
              builder: (context, snapshot) {
                if (snapshot.hasError) {
                  return const Text('Something went wrong');
                }
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return const CircularProgressIndicator();
                }
                return DataTable(
                  headingRowColor: MaterialStateColor.resolveWith(
                      (states) => const Color(0xFF2c3237)),
                  dataRowColor: MaterialStateColor.resolveWith(
                      (states) => const Color(0xFF1f2327)),
                  columns: const [
                    DataColumn(
                        label: Text('Player',
                            style:
                                TextStyle(color: Colors.white, fontSize: 11))),
                    DataColumn(
                        label: Text('Date',
                            style:
                                TextStyle(color: Colors.white, fontSize: 11))),
                    DataColumn(
                        label: Text('Duration',
                            style:
                                TextStyle(color: Colors.white, fontSize: 11))),
                    DataColumn(
                        label: Text('Result',
                            style:
                                TextStyle(color: Colors.white, fontSize: 11))),
                    DataColumn(
                        label: Text('MID',
                            style: TextStyle(
                                color: Colors.white,
                                fontSize: 11))), // Abbreviated "MatchID"
                    DataColumn(
                        label: Text('PGN',
                            style: TextStyle(
                                color: Colors.white,
                                fontSize: 11))), // Abbreviated "Image"
                  ],
                  rows: snapshot.data!.docs
                      .map<DataRow>((DocumentSnapshot document) {
                    Map<String, dynamic> data =
                        document.data()! as Map<String, dynamic>;
                    return DataRow(
                      cells: [
                        DataCell(Text(data['Player'] ?? 'Unknown')),
                        DataCell(Text(data['Date'] ?? 'N/A')),
                        DataCell(Text(data['Duration'] ?? 'N/A')),
                        DataCell(Text(data['Result'] ?? 'N/A')),
                        DataCell(Text(data['MatchID']?.toString() ?? 'N/A')),
                        DataCell(
                          GestureDetector(
                            onTap: () async {
                              final url = data['PGN'];
                              if (await canLaunch(url)) {
                                await launch(url);
                              } else {
                                ScaffoldMessenger.of(context).showSnackBar(
                                  SnackBar(
                                      content: Text('Could not launch $url')),
                                );
                              }
                            },
                            child: const Icon(Icons.image, color: Colors.white),
                          ),
                        ),
                      ],
                    );
                  }).toList(),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
