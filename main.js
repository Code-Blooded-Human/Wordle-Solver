class Box{
    constructor(name,letter='O'){
        this.name = name;
        this.color = '#eeeeee';
        this.colors = ['#eeeeee', '#29AB87', '#f1ff62']
        this.state = 0;
        let html = "<div class='box' id='"+name+"'>"+letter+"</div>";
        let box = this;
        
        $("#main-container").append(html);
        
        $("#"+name).click(()=>{
            box.state++;
            box.state=box.state%3;
            this.color = this.colors[this.state];
            $("#"+name).css('background-color',this.color);
        })
    }
}

let box1 = new Box('box1','H');
let box2 = new Box('box2','E');
let box3 = new Box('box3','L');
let box4 = new Box('box4','L');
let box5 = new Box('box5','O');


console.log("JS running");