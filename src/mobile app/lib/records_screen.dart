import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/services.dart'; // For using Clipboard

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
                      style: TextStyle(color: Colors.white, fontSize: 9));
                },
              ),
            ),
            const SizedBox(height: 32),
            StreamBuilder<QuerySnapshot>(
              stream: recordsRef.snapshots(),
              builder: (context, snapshot) {
                if (snapshot.hasError) {
                  return const Text('Something went wrong',
                      style: TextStyle(color: Colors.white, fontSize: 9));
                }
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return const CircularProgressIndicator();
                }
                return LayoutBuilder(
                  builder: (context, constraints) {
                    return SingleChildScrollView(
                      scrollDirection: Axis.horizontal,
                      child: ConstrainedBox(
                        constraints:
                            BoxConstraints(minWidth: constraints.maxWidth),
                        child: DataTable(
                          headingRowColor: MaterialStateColor.resolveWith(
                              (states) => const Color(0xFF2c3237)),
                          dataRowColor: MaterialStateColor.resolveWith(
                              (states) => const Color(0xFF1f2327)),
                          columns: const <DataColumn>[
                            DataColumn(
                                label: Text('Player',
                                    style: TextStyle(
                                        color: Colors.white, fontSize: 10))),
                            DataColumn(
                                label: Text('Date',
                                    style: TextStyle(
                                        color: Colors.white, fontSize: 10))),
                            DataColumn(
                                label: Text('Duration',
                                    style: TextStyle(
                                        color: Colors.white, fontSize: 10))),
                            DataColumn(
                                label: Text('Result',
                                    style: TextStyle(
                                        color: Colors.white, fontSize: 10))),
                            DataColumn(
                                label: Text('MID',
                                    style: TextStyle(
                                        color: Colors.white, fontSize: 10))),
                            DataColumn(
                                label: Text('PGN',
                                    style: TextStyle(
                                        color: Colors.white, fontSize: 10))),
                          ],
                          rows: _buildDataRow(snapshot.data!.docs, context),
                        ),
                      ),
                    );
                  },
                );
              },
            ),
          ],
        ),
      ),
    );
  }

  List<DataRow> _buildDataRow(
      List<DocumentSnapshot> docs, BuildContext context) {
    return docs.map<DataRow>((DocumentSnapshot document) {
      Map<String, dynamic> data = document.data()! as Map<String, dynamic>;
      return DataRow(cells: <DataCell>[
        DataCell(Text(data['Player'] ?? 'Unknown',
            style: TextStyle(color: Colors.white, fontSize: 10),
            textAlign: TextAlign.center)),
        DataCell(Text(data['Date'] ?? 'N/A',
            style: TextStyle(color: Colors.white, fontSize: 10),
            textAlign: TextAlign.center)),
        DataCell(Text(data['Duration'] ?? 'N/A',
            style: TextStyle(color: Colors.white, fontSize: 10),
            textAlign: TextAlign.center)),
        DataCell(Text(data['Result'] ?? 'N/A',
            style: TextStyle(color: Colors.white, fontSize: 10),
            textAlign: TextAlign.center)),
        DataCell(Text(data['MatchID']?.toString() ?? 'N/A',
            style: TextStyle(color: Colors.white, fontSize: 10),
            textAlign: TextAlign.center)),
        DataCell(
          Center(
            child: IconButton(
              icon: const Icon(Icons.content_copy, color: Colors.white),
              onPressed: () {
                Clipboard.setData(
                    ClipboardData(text: data['PGN']?.toString() ?? 'N/A'));
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text('PGN copied to clipboard',
                        style: TextStyle(color: Colors.white, fontSize: 10)),
                    backgroundColor: Color(0xFF323739),
                  ),
                );
              },
            ),
          ),
        ),
      ]);
    }).toList();
  }
}
