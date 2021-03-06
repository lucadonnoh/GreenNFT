<script>

    console.log("A")
    import results from "../../static/results.json"
    console.log("B")

    //let results = require('../../../results.json');
    import SvelteTable from "svelte-table";

    const columns = [
        {
            key: "name",
            title: "Name",
            value: (v) => v.name,
            sortable: true,
            renderValue: (v) => {
                if("name" in v) {
                    if("url" in v) {
                        return "<a href=\"" + v.url + "\">" + v.name + "</a>";
                    }
                    else{
                        return v.name;
                    }
                }
                else {
                    return "N/A";
                }
            } 
        },
        {
            key: "create",
            title: "Create",
            value: (v) => "create" in v ? v.create.median : "N/A",
            sortable: true
        },
        {
            key: "buy",
            title: "Buy",
            value: (v) => "buy" in v ? v.buy.median : "N/A",
            sortable: true
        },
        {
            key: "transfer",
            title: "Transfer",
            value: (v) => "transfer" in v ? v.transfer.median : "N/A",
            sortable: true
        },
        {
            key: "bid",
            title: "Bid",
            value: (v) => "bid" in v ? v.bid.median : "N/A",
            sortable: true
        }
    ];
    const data = results;
</script>

<h1>Home</h1>
<p>This is the home</p>

<SvelteTable
  classNameTable="table"
  columns={columns}
  rows={data}/>