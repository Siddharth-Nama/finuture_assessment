import React from 'react';

const FileUploader = ({ onUpload, isLoading }) => {
  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      onUpload(e.target.files[0]);
    }
  };

  return (
    <div className="w-full">
      <label className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100 transition-colors">
        <div className="flex flex-col items-center justify-center pt-5 pb-6">
          <p className="mb-2 text-sm text-gray-500"><span className="font-semibold">Click to upload</span> or drag and drop</p>
          <p className="text-xs text-gray-500">PDF (MAX. 10MB)</p>
        </div>
        <input type="file" className="hidden" accept=".pdf" onChange={handleFileChange} disabled={isLoading} />
      </label>
      {isLoading && <p className="mt-2 text-center text-blue-500">Processing...</p>}
    </div>
  );
};

export default FileUploader;
