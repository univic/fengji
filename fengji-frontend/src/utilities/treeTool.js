
// do recursive search throughout a tree structure

function treeSearch(tree, recursiveOnProperty, SearchOnProperty, searchValue) {
  let returnValue = null;
  // conduct search at 1st level
  tree.forEach((item) => {
    if (item[SearchOnProperty] === searchValue) {
      returnValue = item;
    } else {
      // if nothing is found, do recursive search
      if (Object.prototype.hasOwnProperty.call(item, recursiveOnProperty) && item[recursiveOnProperty] instanceof Array && item[recursiveOnProperty].length > 0) {
        returnValue = treeSearch(item[recursiveOnProperty], recursiveOnProperty, SearchOnProperty, searchValue)
      }
    }
  });
  return returnValue;

}


export default {
  treeSearch,
}