

export default function InventoryList({inventory, ...props}) {

  let rows = inventory?.map((item, index) =>{
    return(
      <tr key={item.id}>
        <td>{ item.id }</td>
        <td>{ item.name }</td>
      </tr>
    )
  })

  return(
    <table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Name</th>
        </tr>
      </thead>

      <tbody> 
        { rows }
      </tbody>

      <tfoot>
        <tr>
          <td colSpan={2}>{ inventory?.length || 0 } </td>
        </tr>
      </tfoot>

    </table>
  );
}