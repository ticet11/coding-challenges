const headingGenerator = (title, typeOfHeading) => {
    return `<h${typeOfHeading}>${title}</h${typeOfHeading}>`
}

headingGenerator('hi, there', 1) // <h1>hi, there</h1>