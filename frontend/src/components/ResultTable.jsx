import React from 'react';

const ResultTable = ({ data }) => {
  if (!data) return null;

  const rows = [
    { label: 'Policy Number', value: data.policy_number },
    { label: 'Holder Name', value: data.holder_name },
    { label: 'Premium Amount', value: data.premium_amount },
    { label: 'Sum Assured', value: data.sum_assured },
    { label: 'Start Date', value: data.coverage_start_date },
    { label: 'End Date', value: data.coverage_end_date },
  ];

  return (
    <div className="mt-8 overflow-hidden shadow ring-1 ring-black ring-opacity-5 sm:rounded-lg">
      <table className="min-w-full divide-y divide-gray-300">
        <thead className="bg-gray-50">
          <tr>
            <th scope="col" className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">Field</th>
            <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Value</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-200 bg-white">
          {rows.map((row) => (
            <tr key={row.label}>
              <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">{row.label}</td>
              <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{row.value || '-'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ResultTable;
