import { useState } from 'react';
import axios from 'axios';
import { AlertCircle } from 'lucide-react';
import FileUploader from './components/FileUploader';
import ResultTable from './components/ResultTable';

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleUpload = async (file) => {
    setLoading(true);
    setError(null);
    setResult(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/api/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      const data = response.data;
      if (data.extracted_data && data.extracted_data.length > 0) {
          setResult(data.extracted_data[0]);
      } else {
          setError("No data extracted.");
      }
    } catch (err) {
      console.error(err);
      setError("Upload failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-10">
          <h1 className="text-3xl font-bold text-gray-900">Insurance Policy Parser</h1>
          <p className="mt-2 text-gray-600">Upload your policy document to extract key details.</p>
        </div>

        <div className="bg-white p-8 rounded-xl shadow-lg">
          <FileUploader onUpload={handleUpload} isLoading={loading} />
          
          {error && (
            <div className="mt-4 p-4 bg-red-50 text-red-700 rounded-md flex items-center">
              <AlertCircle className="w-5 h-5 mr-2" />
              {error}
            </div>
          )}

          {result && <ResultTable data={result} />}
        </div>
      </div>
    </div>
  );
}

export default App;
